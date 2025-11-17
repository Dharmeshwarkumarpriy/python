from oops.inheritence.carOfEmployee.Car import Car
class Employee:
    eName="dharam"
    eNumber="987640355"

    def emp(self):
        print("emp name:",self.eName)
        print("emp no:",self.eNumber)
        print("car info:")
        self.carDetail()

    def __init__(self):
        self.car=Car() # object of Car class ...

    def carDetail(self):  # Car class Property ...
        print("car name:",self.car.cName)
        print("car model:",self.car.model)
        print("car color:")
        self.car.color()

# show the value by ref ...
e=Employee()
e.emp()
# print("car details...")
# e.carDetail()