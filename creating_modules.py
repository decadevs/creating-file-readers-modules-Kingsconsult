from abc import ABC, abstractmethod


class FileInterface(ABC):

    @abstractmethod
    def read_all_lines(self):
        pass

    @abstractmethod
    def read_first_two_lines(self):
        pass
    
    @abstractmethod
    def read_last_two_lines(self):
        pass


class ReadBytesFromFile(FileInterface):
    def __init__(self, filename, mode = 'r'): 
        self.filename = open(filename)
        self.file = None

    def __iter__(self):
        return self.filename

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as file2:
            for line in file2:
                yield line

    def __enter__(self):
        self.filename = open(self.filename, 'r')
        return self.filename

    def __next__(self):
        return next(self.file)

    def read_all_lines(self):
        # self.file.seek(0)
        # for line in self.filename:
        #     print(line)
        pass

    def read_first_two_lines(self):
        pass

    def read_last_two_lines(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


a = ReadBytesFromFile('iris.csv')
# print(next(a.read_file('iris.csv')))
print(next(a.read_file('iris.csv')))
print(next(a.read_file('iris.csv')))



# loading a file
with open('iris.csv', 'r') as file2:
#     file2.readlines()


# with open('iris.csv', 'r') as file2:
#     for line in file2:
#         print(line)


            # print(line)


# a = read_file('iris.csv')
# print(next(a))
# print(next(a))
# print(next(a))