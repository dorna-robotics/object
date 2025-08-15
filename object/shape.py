import numpy as np
from dorna2 import Pose
from dorna2 import pose as dorna_pose


class Sphere(Pose):
    def __init__(self, name="sphere", num_sample=50, num_sub_sample=8, radius=250, hemisphere='south', cap_deg=10, pose=None, parent=None):
        num_sub_sample = max(1, num_sub_sample)  # ensure at least one sub-sample
        anchors = {
            "o": [0, 0, 0, 0, 0, 0],
        }
        
        # samples
        T_s = sample_spherical_cap_fibonacci_T(num_sample, radius, cap_deg, hemisphere=hemisphere)

        # create anchors
        for i in range(len(T_s)):
            local = dorna_pose.T_to_xyzabc(T_s[i])
            for j in range(num_sub_sample):
                angle = j * (360 / num_sub_sample)
                abc_j = dorna_pose.rotate_abc(local[3:6], [0, 0, 1], angle, local=True)
                anchors[f"p_{i}_{j}"] = local[:3] + abc_j

        # add sub-samples
        super().__init__(name, pose, parent, anchors)


def sample_spherical_cap_fibonacci_T(n, radius, cap_deg, hemisphere='north'):
    """
    n: number of poses
    radius: sphere radius
    cap_deg: half-angle of spherical cap measured from the pole axis (degrees)
    hemisphere: 'north' => cap around +Z, 'south' => cap around -Z
    returns: list of 4x4 numpy arrays (homogeneous transforms)
    """
    # golden angle and cap z limits
    ga = np.pi * (3.0 - np.sqrt(5.0))
    cap_cos = np.cos(np.radians(cap_deg))
    
    if hemisphere.lower() == 'north':
        z_min, z_max = cap_cos, 1.0
    elif hemisphere.lower() == 'south':
        z_min, z_max = -1.0, -cap_cos
    else:
        raise ValueError("hemisphere must be 'north' or 'south'")
    
    # uniform in z for spherical cap
    i = np.arange(n)
    z = z_min + (z_max - z_min) * (i + 0.5) / n
    theta = np.arccos(z)
    phi = (i * ga) % (2.0 * np.pi)
    
    st = np.sin(theta)
    x = radius * st * np.cos(phi)
    y = radius * st * np.sin(phi)
    zc = radius * z
    P = np.stack([x, y, zc], axis=1)
    
    # orientations: tool +Z points to origin; +X in plane of world +Z
    zt = -P / np.linalg.norm(P, axis=1, keepdims=True)
    k = np.array([0.0, 0.0, 1.0])
    dotk = zt @ k
    K = np.repeat(k[None, :], n, axis=0)
    K[np.abs(dotk) > 0.999] = np.array([1.0, 0.0, 0.0])
    
    x_tmp = K - (dotk[:, None]) * zt
    x_tmp /= np.linalg.norm(x_tmp, axis=1, keepdims=True)
    yt = np.cross(zt, x_tmp); yt /= np.linalg.norm(yt, axis=1, keepdims=True)
    xt = np.cross(yt, zt);   xt /= np.linalg.norm(xt, axis=1, keepdims=True)
    
    # build 4x4 transforms
    Ts = []
    for j in range(n):
        T = np.eye(4)
        T[0:3, 0] = xt[j]
        T[0:3, 1] = yt[j]
        T[0:3, 2] = zt[j]
        T[0:3, 3] = P[j]
        Ts.append(T)
    return Ts