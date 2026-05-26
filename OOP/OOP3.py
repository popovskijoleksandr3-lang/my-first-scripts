class Tank:
    def __init__(self,name,armour):
        self.name=name
        self.armour=armour
    def vehicle(self):
        print(f"This is a tank named {self.name} and its armor is {self.armour} millimeters.")
Tank1=Tank("T72",600)
Tank1.vehicle()
