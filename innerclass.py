class student:


    def __init__(self,name,rollno):
        self.name = name
        self.rollno  = rollno
        self.laptop = self.laptop()
    def show(self):
        print(self.name, self.rollno)
        self.laptop.show()
    class laptop:

        def __init__(self):
            self.brand = "hp"
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            print(self.brand,self.ram,self.cpu)
s1 = student ('loki',5)
s2 = student ('manu',4)

s1.show()
