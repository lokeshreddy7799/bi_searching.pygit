from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("its running")
class whiteboard:
    def write(self):
        print("its wrriting")
class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()

com1 = laptop()
com1.process()
prog1 = programmer()
prog1.work(com1)



com1 = laptop()








