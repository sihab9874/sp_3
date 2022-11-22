import unittest 
from speciallecture.ss2022 import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read1(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        self.assertEqual(4, len(l))

    def test_read2(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        print(l[1][1])
        self.assertEqual(" 123", l[1][1])


    def test_read3(self):
        with self.assertRaises(Exception):
            printer = CSVPrinter("tests/samle.csv")
            printer.read()


            