from spreadsheet_interface import SpreadsheetInterface
import numpy as np
import pandas as pd

class TsvSpreadsheet(SpreadsheetInterface):

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file1 = self.filename

    def __enter__(self):
        self.file1 = pd.read_csv(self.file1)
        return self.file1

    def __iter__(self):
        return self.file1

    # def read_all_rows(self):
    #     data = pd.read_csv(self.file1)
    #     for datas in data:
    #         yield datas
    #     # return data
    def read_all_rows(self):
        pass


    def read_first_two_rows(self):
        data = pd.read_csv(self.file1, sep='\t')
        return data.head(2)

    def read_last_two_rows(self):
        data = pd.read_csv(self.file1, sep='\t')
        return data.tail(2)

    def __next__(self):
        return next(self.file1)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file1.close()




a = TsvSpreadsheet('kings.tsv', 'r')
print(a.read_all_rows())
# print(a.read_first_two_rows())
# print(a.read_last_two_rows())
