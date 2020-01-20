import unittest

from spreadsheet.csv_spreadsheet import CsvSpreadsheet 

a = CsvSpreadsheet('iris.csv', 'r')

class TestClass(unittest.TestCase):
    
    def test(self):
        self.assertEquals(a.read_all_rows('iris.csv'))

