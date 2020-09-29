'''
Create a class called Vehicle, which will have a property called Speed
​​and a method called Accelerate, the Speed property is initialized
to zero and when the Accelerate method is called the Speed property
must increase by one. So, print the initial value of the Speed property,
then call the Accelerate method & print the value of the Speed property again.
Repeat this three times.
'''


class Vehicle:

    def __init__(self, speed):
        self.speed = speed

    def accelerate(self):
        self.speed += 1


car = Vehicle(0)
print(f'My car speed is {car.speed} kmph. Lets accelerate')
car.accelerate()
print(f'Now the speed is {car.speed} kmph. More!!!')
car.accelerate()
print(f'New speed is {car.speed} kmph. More??')
car.accelerate()
print(f'Haha!! Car goes brrrr at {car.speed} kmph.')
