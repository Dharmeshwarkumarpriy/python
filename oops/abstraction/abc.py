from abc import abstractmethod

from abc import *

class Test:
    pass
t=Test()

class Test1(ABC):
    pass
t1=Test1()

class Test2(ABC):
    @abstractmethod
    def m1(self):
        pass
t2=Test()

class Test3():
    @abstractmethod
    def m1(self):
        pass
t3=Test()