class student:
    school = "gtpl"
    def __init__(self,m1,m2,m3):
         self.m1=m1
         self.m2=m2
         self.m3=m3
    def avg(self):
         return(self.m1 + self.m2 + self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,valu):
        self.m1 = value
s1 = student(34,56,78)
s2 = student(28,45,89,)
print(s1.avg())
print(s2.avg())



class student:
    school = "gtpl"
    def __init__(self,m1,m2,m3):
         self.m1=m1
         self.m2=m2
         self.m3=m3
    def avg(self):
         return(self.m1 + self.m2 + self.m3)/3
    @classmethod
    def info(cls):
        return cls.school


s1 = student(34,56,78)
s2 = student(28,45,89,)
print(s1.avg())
print(s2.avg())
print(student.info())
