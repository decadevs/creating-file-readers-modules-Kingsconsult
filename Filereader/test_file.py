from interface import FileInterface

class TxtFile(FileInterface):
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file1 = open(self.filename, 'r')

    def __enter__(self):
        self.file1 = open(self.filename, 'r')
        return self.file1

    def __iter__(self):
        return self.file1

    def read_all_lines(self):
        for line in self.file1:
            yield line
            # print(line)
            # return line


    def read_first_two_lines(self):
        kk = self.file1.readlines()
        return kk[1], kk[2]


    # def read_first_two_lines(self):
    #     for line, fil in zip(range(2), self.file1):
    #         # yield fil
    #         print(fil)
    #     # return self

    def read_last_two_lines(self):
        fileline = self.file1.readlines()
        lastline = fileline[len(fileline) - 1]
        second_lastline = fileline[len(fileline) - 2]
        return lastline, second_lastline

    def __next__(self):
        return next(self.file1)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file1.close()


a = TxtFile('iris.csv', 'r')
# print(next(a.read_all_lines()))
# print(next(a.read_all_lines()))
print((a.read_all_lines()))
# print(next(a.read_all_lines()))
print(a.read_first_two_lines())
# print(a.read_all_lines())





