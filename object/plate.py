from dorna2 import Pose

class Charuco_plate(Pose):
    def __init__(self, name="charuco_plate", pose=None, parent=None):
        anchors = {
            "o": [-5, -5, 0, 0, 0, 0],
            "xy": [215, 215, 0, 0, 0],
            "x": [215, 0, 0, 0, 0, 0],
            "y": [0, 215, 0, 0, 0, 0],
        }
        super().__init__(name, pose, parent, anchors)
