from abc import ABC,abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Engine):
    def start(self):
        print("Starting")
    def stop(self):
        print("stop")
    def drive(self):
        self.start()
        self.stop()

car=Car()
car.drive()


