'''
Make a class called Person, which will have three properties: Name, Surname
and Age. Then, create an instance of that class, assign values ​​to its
properties with data of a person (Name, Surname and Age) and then print each
of the properties of the instance of the Person class.
'''


class Person:

    name = ''
    surname = ''
    age = 0

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


print(f'My name is {Person.name} {Person.surname} and my age is {Person.age}.')
p1 = Person('Micheal', 'Scott', 32)
print(f'My name is {p1.name} {p1.surname} and my age is {p1.age}.')
