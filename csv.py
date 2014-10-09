__author__ = 'Olzhas'

import csv

def csv_reader(file_object):
    """

    CSV file reader
    """
    reader = csv.reader(file_object)
    for row in reader:
        print (" ".join(row))

if __name__=="__main__":
    csv_path="TB.csv"
    with open(csv_path, 'rb') as f_obj:
        csv_reader(f_obj)
