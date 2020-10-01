'''
Taking advantage of the File class we are going to create another static
 method called Exists on top of the already created Read method. This new
 Exists method receives a parameter of the string type called FilePath and
 returns a Boolean, true if the file exists and false otherwise.
'''
import os


class File:

    fileContent = ''

    @staticmethod
    def is_exist(filePath):
        return os.path.exists(filePath)

    @staticmethod
    def read(filePath):
        file_handle = open(filePath, 'r')
        fileContent = file_handle.read()
        file_handle.close()
        return fileContent


print(File.is_exist('exercise12.py'))
print(File.is_exist('exercise1.py'))
print(File.read('exercise1.py'))
