'''
Make a class called Person, which will have five properties: Name, Surname, Age, Place and Hobby.
Then, create an instance of that class, assign values ​​to its
properties with data of a person (Name, Surname and Age) and then print each
of the properties of the instance of the Person class.
'''


class Person:

    name = ''
    surname = ''
    age = 0
    place = ''
    hobby = ''

    def __init__(self, name, surname, age, place, hobby):
        self.name = name
        self.surname = surname
        self.age = age
        self.place = place
        self.hobby = hobby

print(f'My name is {Person.name} {Person.surname} and my age is {Person.age}. I am from {Person.place} and my hobby is {Person.hobby}')
p1 = Person('Micheal', 'Scott', 32, 'US', 'Swimming')
print(f'My name is {p1.name} {p1.surname} and my age is {p1.age}.')
