class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print(name,"walk with",cls.legs,"legs")

Animal.walk("Dog")
Animal.walk("cow")