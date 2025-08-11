from dorna2 import Pose

class Charuco_board(Pose):
    def __init__(self, name="Charuco_board", pose=None, parent=None):
        anchors = {
            "o": [-5, -5, 3, 0, 0, 0],
            "xy": [215, 215, 3, 0, 0, 0],
            "x": [215, 0, 3, 0, 0, 0],
            "y": [0, 215, 3, 0, 0, 0],
        }

        for i in range(3):
            anchors[str(i)] = [(2*i+1)*30+3, 0, 0, 0, 0, 0]
        for i in range(4):
            anchors[str(3+i)] = [(2*i)*30+3, (1)*30+3, 0, 0, 0, 0]
        for i in range(3):
            anchors[str(7+i)] = [(2*i+1)*30+3, (2)*30+3, 0, 0, 0, 0]
        for i in range(4):
            anchors[str(10+i)] = [(2*i)*30+3, (3)*30+3, 0, 0, 0, 0]
        for i in range(3):
            anchors[str(14+i)] = [(2*i+1)*30+3, (4)*30+3, 0, 0, 0, 0]
        for i in range(4):
            anchors[str(17+i)] = [(2*i)*30+3, (5)*30+3, 0, 0, 0, 0]
        for i in range(3):
            anchors[str(21+i)] = [(2*i+1)*30+3, (6)*30+3, 0, 0, 0, 0]


        super().__init__(name, pose, parent, anchors)
