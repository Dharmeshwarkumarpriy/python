class OverWeight(Exception):
    def __init__(self,arg):
        self.msg=arg

class UnderWeight(Exception):
    def __init__(self,arg):
        self.msg=arg

weight=int(input("enter the weight:"))
if weight>80:
    raise OverWeight("fat and obese person")
elif weight<40:
    raise  UnderWeight("sick and thin person")
else:
    print("normal person")