class Parent:
    def many(self):
        print("dimple")

class Child(Parent):
    def many(self):
        super().many()
        print("katrina kaif")

c=Child()
c.many()