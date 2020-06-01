import csv
import time

with open(r'.\configs\file1.csv', 'r') as t1, open(r'.\configs\file2.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

fileName = f'.\\configs\\{time.strftime("%Y%m%d-%H%M%S")}.csv'
with open(fileName, 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)