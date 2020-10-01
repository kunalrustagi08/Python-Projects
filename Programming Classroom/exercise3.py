'''
Create a class called Calculator. This class will have four static methods:

Add()
Subtract()
Multiply()
Divide()

Each method will receive two parameters: "num1" and "num2" and will return the
result of the corresponding arithmetic operation.
Example: The static addition method will return the sum of num1 and num2. Then,
you must choose numbers of your preference and perform an operation with them
for each method, for example, you can choose 10 and 50 to make the sum.

Print the result of each method.
'''


class Calculator:

    @staticmethod
    def add(num1, num2):
        sum = num1 + num2
        return sum

    @staticmethod
    def subtract(num1, num2):
        dif = num1 - num2
        return dif

    @staticmethod
    def multiply(num1, num2):
        prod = num1 * num2
        return prod

    @staticmethod
    def divide(num1, num2):
        quo = format((num1 / num2), '.2f')
        return quo

    @staticmethod
    def int_divide(num1, num2):
        int_quo = num1 // num2
        return int_quo

    @staticmethod
    def remainder(num1, num2):
        rem = num1 % num2
        return rem


print(f'Sum is {Calculator.add(10,50)}')
print(f'Difference is {Calculator.subtract(50, 30)}')
print(f'Product is {Calculator.multiply(1,0)}')
print(f'Division equals {Calculator.divide(10,3)}')
print(f'Integer Division equals {Calculator.int_divide(10,3)}')
print(f'Remainder equals {Calculator.remainder(10,3)}')
