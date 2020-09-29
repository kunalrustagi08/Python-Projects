'''
Simulate a basic fruit store that has three products:
 Banana, Apple and Orange.

You must create a class called Fruit that receives three parameters:
 Name of the fruit, price of the fruit, and expiration date.

You must create each fruit using the Fruit class and passing the name of each
 fruit to the instance of that class and invent a price and expiration date
 for each one.

Print the details for each fruit.
'''


class Fruit:

    def __init__(self, name, price, expiry_date):
        self.name = name
        self.price = price
        self.expiry_date = expiry_date

    def details(self):
        print(f'Name of fruit: {self.name}')
        print(f'Price of {self.name}: {self.price}')
        print(f'Expiration date: {self.expiry_date}')


banana = Fruit('Banana', 10, '02-10-2020')
apple = Fruit('Apple', 35, '09-10-2020')
orange = Fruit('Orange', 20, '30-09-2020')

banana.details()
orange.details()
apple.details()
