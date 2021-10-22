class Vehicle:
    def general_usage(self):
        print("general use:transportation")
class car(Vehicle):
    def __init__ (self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("specific use: road trip,racing")
c = car()
c.general_usage()
c.specific_usage()

m = MotorCycle()
m.general_usage()
m.specific_usage()