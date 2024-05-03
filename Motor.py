class Motor():
    def __init__(self, pinV, pinCOM, pinPMW, value):
        self.pinV = pinV
        self.pinCOM = pinCOM
        self.pinPMW = pinPMW
        self.value = None
    
    def Rotation(self):
        print(f"Rotation angle : {self.value}")
