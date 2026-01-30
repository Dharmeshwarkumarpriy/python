class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

    def move(self):
        print("sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand=brand
        self.model= model

    def move(self):
        print("fly!")

car1 =Car("ford", "mustang")

boat1 =Boat("Ibiza","touring 20")

plane1 = Plane("boeing","789")

for x in (car1, boat1, plane1):
    x.move()