class Student:
    education = "Step"

    def __init__(self, age, height=120, name='Oleg'):
        self.name = name
        self.age = age
        self.height = height
        print("__inin__")

st1 = Student(13)
print(st1.name)
print(st1.age)
print(st1.height)
print(st1.education)
st1.height = 135
print(st1.height)
st2 = Student(15, 155, 'Sergiy')
print(st2.name)
print(st2.age)
print(st2.height)