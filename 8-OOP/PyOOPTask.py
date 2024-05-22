class Shape:
    def __init__(self, shapeX, shapeY, shapeZ, shapeC, shapeS):
        self.shapeX = shapeX  # X of shape origin
        self.shapeY = shapeY  # Y of shape origin
        self.shapeZ = shapeZ  # Z of shape origin
        self.shapeC = shapeC  # Colour of shape
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
    def VECTOR(self):
        return f"V:{self.shapeX},{self.shapeY},{self.shapeZ},{self.shapeC}"

    @classmethod
    def INFO(self):
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
    def shapeX(self):
        return self._shapeX

    @shapeX.setter
    def shapeX(self, shapeX):
        self._shapeX = shapeX

    @property
    def shapeY(self):
        return self._shapeY

    @shapeY.setter
    def shapeY(self, shapeY):
        self._shapeY = shapeY

    @property
    def shapeZ(self):
        return self._shapeZ

    @shapeZ.setter
    def shapeZ(self, shapeZ):
        self._shapeZ = shapeZ

    @property
    def shapeC(self):
        return self._shapeC

    @shapeC.setter
    def shapeC(self, shapeC):
        self._shapeC = shapeC

    @property
    def shapeS(self):
        return self._shapeS

    @shapeS.setter
    def shapeS(self, shapeS):
        self._shapeS = shapeS

####################################################################################################################
