from dorna2 import Pose

class Dorna_TA(Pose):
    def __init__(self, name="dorna_TA", pose=None, parent=None):
        anchors = {
            "0": [35, 50, 0, 0, 0, 0],
            "1": [35, -50, 0, 0, 0, 0],
            "2": [-15, 50, 0, 0, 0, 0],
            "3": [-15, -50, 0, 0, 0, 0],
            "4": [-65, 50, 0, 0, 0, 0],
            "5": [-65, -50, 0, 0, 0, 0],
            "6": [-115, 50, 0, 0, 0, 0],
            "7": [-115, -50, 0, 0, 0, 0]
        }
        super().__init__(name, pose, parent, anchors)



class Fixture_plate(Pose):
    """
    A grid plate with labeled holes as anchors (A1..J20 by default).
    - All holes are exposed as anchors with names like "A1", "B7", etc.
    - Optional "connection" anchors are added at half-pitch offsets on selected edges
      to support your legacy snap points (A3/A8/A13/A18, J3/J8/J13/J18, C1/H1, C20/H20).
    """
    def __init__(
        self,
        name="fixture_plate",
        pose=None,
        parent=None,
        hole_pitch=25,
    ):
        # holes
        anchors = {}
        rows = [chr(c) for c in range(ord('A'), ord('J')+1)]
        for i, row in enumerate(rows):
            for n in range(1, 21):
                label = f"{row}{n}"
                x = (n - 1) * hole_pitch
                y = i * hole_pitch
                anchors[label] = [x+0.5*(hole_pitch), -y+4.5*(hole_pitch), 0, 0, 0, 0]
        
        # mates
        for hole in ["A3", "A8", "A13", "A18"]:
            anchors["mate_"+hole] = list(anchors[hole])
            anchors["mate_"+hole][1] += hole_pitch/2

        for hole in ["J3", "J8", "J13", "J18"]:
            anchors["mate_"+hole] = list(anchors[hole])
            anchors["mate_"+hole][1] += -hole_pitch/2

        for hole in ["C1", "H1"]:
            anchors["mate_"+hole] = list(anchors[hole])
            anchors["mate_"+hole][0] += -hole_pitch/2

        for hole in ["C20", "H20"]:
            anchors["mate_"+hole] = list(anchors[hole])
            anchors["mate_"+hole][0] += hole_pitch/2


        super().__init__(name, pose, parent, anchors)


class Tool_changer(Pose):
    def __init__(self, name="tool_changer", pose=None, parent=None):
        anchors = {
            "A2": [-25, -25, 0, 0, 0, 0],
            "B1": [25, 25, 0 , 0, 0, 0],
            "connect": [-46, 0, 167.5, 180, 0, 0],
        }
        super().__init__(name, pose, parent, anchors)