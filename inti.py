class computer:
    def __int__(self):
        print("in init")
    def config(self):
        print("i5, 16gb ,1tb")
com1= computer()
com2= computer()
com1.config()
com2.config()






class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("config is ", self.cpu, self.ram)
com1 = computer('i5',16)
com2 = computer("ryzen 3",8)



com1.config()
com2.config()






