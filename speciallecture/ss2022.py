import csv

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name
    # FIXME: catch the right exception, log it, and raise
    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines