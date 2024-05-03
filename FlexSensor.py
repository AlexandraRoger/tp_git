class FlexSensor():
    def __init__(self, finger, pinA, pinB):
        self.finger = finger
        self.pinA = pinA
        self.pinB = pinB
        self.value = None

    def analog_read(self):
        print("Finger : {self.finger} - Flex : {self.value}")