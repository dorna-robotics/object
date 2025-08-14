from dorna2 import Pose

class Charuco_board(Pose):
    def __init__(self, name="Charuco_board", pose=None, parent=None):
        anchors = {
            "o": [-5, -5, 3, 0, 0, 0],
            "xy": [215, 215, 3, 0, 0, 0],
            "x": [215, 0, 3, 0, 0, 0],
            "y": [0, 215, 3, 0, 0, 0],
        }

        # chess corners
        for i in range(8):
            for j in range(8):
                anchors[f"c{i}_{j}"] = [i*30, j*30, 0, 0, 0, 0]
        # aruco
        for i in range(3):
            anchors[f"a_{i}_tl"] = [(2*i+1)*30+3, (0)*30+3, 0, 0, 0, 0]
            anchors[f"a_{i}_tr"] = [(2*i+1)*30+27, (0)*30+3, 0, 0, 0, 0]
            anchors[f"a_{i}_bl"] = [(2*i+1)*30+3, (0)*30+27, 0, 0, 0, 0]
            anchors[f"a_{i}_br"] = [(2*i+1)*30+27, (0)*30+27, 0, 0, 0, 0]
        for i in range(4):
            anchors[f"a_{3+i}_tl"] = [(2*i)*30+3, (1)*30+3, 0, 0, 0, 0]
            anchors[f"a_{3+i}_tr"] = [(2*i)*30+27, (1)*30+3, 0, 0, 0, 0]
            anchors[f"a_{3+i}_bl"] = [(2*i)*30+3, (1)*30+27, 0, 0, 0, 0]
            anchors[f"a_{3+i}_br"] = [(2*i)*30+27, (1)*30+27, 0, 0, 0, 0]
        for i in range(3):
            anchors[f"a_{7+i}_tl"] = [(2*i+1)*30+3, (2)*30+3, 0, 0, 0, 0]
            anchors[f"a_{7+i}_tr"] = [(2*i+1)*30+27, (2)*30+3, 0, 0, 0, 0]
            anchors[f"a_{7+i}_bl"] = [(2*i+1)*30+3, (2)*30+27, 0, 0, 0, 0]
            anchors[f"a_{7+i}_br"] = [(2*i+1)*30+27, (2)*30+27, 0, 0, 0, 0]
        for i in range(4):
            anchors[f"a_{10+i}_tl"] = [(2*i)*30+3, (3)*30+3, 0, 0, 0, 0]
            anchors[f"a_{10+i}_tr"] = [(2*i)*30+27, (3)*30+3, 0, 0, 0, 0]
            anchors[f"a_{10+i}_bl"] = [(2*i)*30+3, (3)*30+27, 0, 0, 0, 0]
            anchors[f"a_{10+i}_br"] = [(2*i)*30+27, (3)*30+27, 0, 0, 0, 0]
        for i in range(3):
            anchors[f"a_{14+i}_tl"] = [(2*i+1)*30+3, (4)*30+3, 0, 0, 0, 0]
            anchors[f"a_{14+i}_tr"] = [(2*i+1)*30+27, (4)*30+3, 0, 0, 0, 0]
            anchors[f"a_{14+i}_bl"] = [(2*i+1)*30+3, (4)*30+27, 0, 0, 0, 0]
            anchors[f"a_{14+i}_br"] = [(2*i+1)*30+27, (4)*30+27, 0, 0, 0, 0]
        for i in range(4):
            anchors[f"a_{17+i}_tl"] = [(2*i)*30+3, (5)*30+3, 0, 0, 0, 0]
            anchors[f"a_{17+i}_tr"] = [(2*i)*30+27, (5)*30+3, 0, 0, 0, 0]
            anchors[f"a_{17+i}_bl"] = [(2*i)*30+3, (5)*30+27, 0, 0, 0, 0]
            anchors[f"a_{17+i}_br"] = [(2*i)*30+27, (5)*30+27, 0, 0, 0, 0]
        for i in range(3):
            anchors[f"a_{21+i}_tl"] = [(2*i+1)*30+3, (6)*30+3, 0, 0, 0, 0]
            anchors[f"a_{21+i}_tr"] = [(2*i+1)*30+27, (6)*30+3, 0, 0, 0, 0]
            anchors[f"a_{21+i}_bl"] = [(2*i+1)*30+3, (6)*30+27, 0, 0, 0, 0]
            anchors[f"a_{21+i}_br"] = [(2*i+1)*30+27, (6)*30+27, 0, 0, 0, 0]

        super().__init__(name, pose, parent, anchors)
