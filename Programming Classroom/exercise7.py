'''
We return to the StringHelper class, here we add another static method called
 Concat, this method receives a single parameter called Args, which is a
 "Pack of parameters", which means that we can pass as many parameters as we
 want, then, within this function there will be A variable called Curr that
 will be initialized as an empty string, and using a for iterator, the
 "Parameters Pack" will be traversed and each parameter will be concatenated
 to Curr variable, after the for it must return the value of the Curr variable.
'''


class StringHelper:

    @staticmethod
    def reverse(originalStr: str):

        return str(originalStr[::-1])

    @staticmethod
    def concat(*args):
        curr = ''
        for arg in args:
            curr += arg

        return curr


print(StringHelper.concat('Hello'))
print(StringHelper.concat('Hello', 'Hector'))
print(StringHelper.concat('Hello', ' ', 'Hector'))
