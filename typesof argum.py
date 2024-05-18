def preson(name,age):

    print(name)
    print(age)
preson("loki",28)


def preson(name,age):

    print(name)
    print(age)
preson(name='loki', age=28)


def display(name, course ='GTPL'):
    print("name :" + name)
    print("course :" , course)
display(course="bse", name="loki")
display(name="suresh")


def print_info(**loki):
    for key, value in loki.items():
        print(key + ":", value)
print_info(name="Alice", age=30, city="New York")







