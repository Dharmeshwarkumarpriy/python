class staticCal:
    roll=102
    @staticmethod
    def display():
        print("class variable is=",staticCal.roll)

    @staticmethod
    def add(x,y):
        print("total a+b =",x+y)

    @staticmethod
    def product(x,y):
        print("product a+b =",x*y)


staticCal.display()

staticCal.add(20,30)
staticCal.product(30,40)

s=staticCal()
s.add(89,90)