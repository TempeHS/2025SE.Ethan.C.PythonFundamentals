class Shape:
    def __init__(self, PosX, PosY, PosZ, ColR, ColG, ColB, shapeS):
        self.PosX = PosX  # X of shape origin
        self.PosY = PosY  # Y of shape origin
        self.PosZ = PosZ  # Z of shape origin
        self.ColR = ColR  # Red Colour of shape
        self.ColG = ColG  # Green Colour of shape
        self.ColB = ColB  # Blue Colour of shape
        self.shapeS = shapeS  # Shape of shape

    def assessShape(self):
        match self.shapeS:
            case "Sphere":
                return 0
            case "Cube":
                return 1
            case "Prism":
                return 2

    @classmethod
    def GetPos(self):
        return f"P:{self.PosX},{self.PosY},{self.PosZ}"

    @classmethod
    def GetCol(self):
        return f"C:{self.ColR},{self.ColG},{self.ColB}"

    @classmethod
    def GetShape(self):
        return f"{self.shapeS}"

    @classmethod
    def CrossSection(self):
        if Shape.assessShape() == 0:

    @classmethod
    def SurfaceArea(self):
        return f"{self.shapeS}"

    @classmethod
    def Volume(self):
        return f"{self.shapeS}"

    @classmethod
    def SurfaceCount(self):
        return f"{self.shapeS}"

#######################################################################################################################

    @property
    def PosX(self):
        return self._PosX

    @PosX.setter
    def PosX(self, PosX):
        self._PosX = int(PosX)

    @property
    def PosY(self):
        return self._PosY

    @PosY.setter
    def PosY(self, PosY):
        self._PosY = int(PosY)

    @property
    def PosZ(self):
        return self._PosZ

    @PosZ.setter
    def PosZ(self, PosZ):
        self._PosZ = int(PosZ)

    @property
    def ColR(self):
        return self._ColR

    @ColR.setter
    def ColR(self, ColR):
        if ColR < 255 and ColR > 0:
            self._ColR = (ColR)
        else:
            raise ValueError("Invalid Red Colour")

    @property
    def ColR(self):
        return self._ColR

    @ColR.setter
    def ColR(self, ColR):
        if ColR < 255 and ColR > 0:
            self._ColR = int(ColR)
        else:
            raise ValueError("Invalid Red Colour")

    @property
    def ColB(self):
        return self._ColB

    @ColB.setter
    def ColB(self, ColB):

    @property
    def shapeS(self):
        return self._shapeS

    @shapeS.setter
    def shapeS(self, shapeS):
        self._shapeS = shapeS

####################################################################################################################
