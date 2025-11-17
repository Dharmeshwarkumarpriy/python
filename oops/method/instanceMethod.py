class Test:
    def __init__(self,name1,marks1):
        self.name="dharmy"
        self.marks="80"

        self.name=name1
        self.marks=marks1
# within the class we can call instance method by using self variable
    # and from outside of the class we can call by using object reference.
    def display(self):
        print("hi",self.name,self.marks)

        #  self.display()

t=Test("yoyo",8)
t.display()
# t.__init__("io",8)