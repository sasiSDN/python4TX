from abc import ABC,abstractmethod

class Excel(ABC):
    def readexcel(self):
        pass

class Browser(Excel):
    @abstractmethod
    def startbrowser(self):
        pass

    @abstractmethod
    def stopbrowser(self):
        pass

class Tc1(Browser):
    def startbrowser(self):
        print("starting")
    def stopbrowser(self):
        print("stop")
    def readexcel(self):
        print("Excel is ready")
    def runTc1(self):
        self.startbrowser()
        self.readexcel()
        self.stopbrowser()
TC1=Tc1()
TC1.runTc1()
