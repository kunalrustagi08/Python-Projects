'''
Taking advantage of the File class we are going to create another static
 method called Delete below the already created Read method. This new Delete
 method receives a string type parameter called FilePath and as its name
 indicates, it deletes the file.
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

    @staticmethod
    def delete(filePath):
        os.remove(filePath)


print(File.delete('abcd.txt'))
