'''
In this exercise (and in some of the following ones) we will work with a
 representation of an auxiliary class, that is, a class that contains
 functions that make certain things easier for the developer.

Create a class called File, which will have a static property called
 FileContent and a static method called Read, which receives as a parameter
 a string called FilePath, then within the Read method a text file will be
 opened with Python, its content will be read , it will be assigned to the
 FileContent variable / property and then the content of FileContent will be
 printed in the same Read function.
'''


class File:

    fileContent = ''

    @staticmethod
    def read(filePath):
        fileContent = open(filePath, 'r')
        print(fileContent.read())


File.read('exercise1.py')
