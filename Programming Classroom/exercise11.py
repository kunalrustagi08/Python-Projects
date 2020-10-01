'''
Here we expand the functionalities of our File class a bit.
Within the Read and Delete methods we must confirm that the file to read
 or delete exists before using it.
In our case, Read will return False if the file does not exist and the
 content of the file if it exists.
In the case of Delete, it will return true if the file exists and false
 otherwise, in addition, in this Delete method if the file exists, we proceed
 to delete it.
'''
import os


class File:

    fileContent = ''

    @staticmethod
    def is_exist(filePath):
        return os.path.exists(filePath)

    @staticmethod
    def read(filePath):
        if File.is_exist(filePath):
            file_handle = open(filePath, 'r')
            fileContent = file_handle.read()
            file_handle.close()
            return fileContent
        return False

    @staticmethod
    def delete(filePath):
        if File.is_exist(filePath):
            os.remove(filePath)
            return True
        return False


print(File.read('exercise1.py'))
print(File.read('abcd.txt'))
print(File.delete('abcd.txt'))
