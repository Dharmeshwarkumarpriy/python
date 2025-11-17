class Duck:
    def talk(self):
        print("quack ... quack")

class Dog:
    def talk(self):
        print("bhooo .... bhooo")

class Cat:
    def talk(self):
        print("meyao....meyaw")

def f1(x):
    x.talk()

l=[Duck(), Cat(), Dog()]
for obj in l:
    f1(obj)
