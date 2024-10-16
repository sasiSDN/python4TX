#ABSTRACTION

from abc import  ABC,abstractmethod

class PyATC(ABC):
    @abstractmethod
    def payfee(self):
        pass

    def enrolled(self):
        print("Enrolled")

class Sasi(PyATC):
    def payfee(self):
        print("Paid")


l=Sasi()
l.enrolled()