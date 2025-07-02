import csv

with open(r"C:\Users\kanza\Downloads\ECMI\Statistic\csv_int.csv", 'r') as csvfile:
    data = list(csv.DictReader(csvfile))
data[:5]

import 