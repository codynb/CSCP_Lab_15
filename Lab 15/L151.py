#The authors are Maggie Dunn and Cody Brown, L151.py

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John",36)

print(p1.name)
print(p1.age)
#this prints:
     # John
     # 36

p2 = Person('Maggie',19)
print(p2.name)
print(p2.age)
#this prints:
     # Maggie
     # 19
