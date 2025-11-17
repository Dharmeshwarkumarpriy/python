from  abc import *
from pydoc import classname


class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        print("pass")

    @abstractmethod
    def disconnect(self):
        print("pass dis")

class Oracle(DBInterface):
    def connect(self):
        print("connecting to oracle DB")

    def disconnect(self):
        print("disconnecting to oracle DB")

class Mysql(DBInterface):
    def connect(self):
        print("connecting to mysql DB")

    def disconnect(self):
        print("disconnecting to mysql DB")

dbname=input("enter database name:")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()