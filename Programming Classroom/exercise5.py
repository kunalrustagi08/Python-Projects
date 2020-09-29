'''
Create a class called StringHelper.

This class will have a static method called Reverse that will receive a
 parameter called "originalStr" of type string and should return that inverted
 string.

Print the value returned by the method.
'''


class StringHelper:

    @staticmethod
    def reverse(originalStr: str):

        return str(originalStr[::-1])


greeting = 'Hello Hector! how are you?'
print(f'{greeting}')
print(f'{StringHelper.reverse(greeting)}')
