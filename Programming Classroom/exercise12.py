'''
We continue with the File class and this time, we will create another static
 method called PathExtension which receives a string type parameter called
 FilePath and verifies if the file exists and in which case it returns the
 file extension (PNG, TXT, MP4, etc) but if the file does not exist it
 returns an empty string.
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

    @staticmethod
    def path_extension(filePath):
        if File.is_exist(filePath):
            return os.path.splitext(filePath)[-1]
        return False


print(File.path_extension('exercise1.py'))
