from dorna2 import Pose

class Charuco_board(Pose):
    def __init__(self, name="Charuco_board", pose=None, parent=None):
        anchors = {
            "o": [-5, -5, 3, 0, 0, 0],
            "xy": [215, 215, 3, 0, 0, 0],
            "x": [215, 0, 3, 0, 0, 0],
            "y": [0, 215, 3, 0, 0, 0],
        }
        super().__init__(name, pose, parent, anchors)
