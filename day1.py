from pathlib import Path
import csv

path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day1.csv'

data = []

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        line = row[0]
        data.append(line)
        
data[0] = 1650
        
for i in range(len(data)):
    data[i] = int(data[i])
    
for i in range(len(data)):
    for j in range(len(data)):
        if i==j:
            continue
        else:
            if data[i] + data[j] == 2020:
                print(data[i] * data[j])
                
                
for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if data[i] + data[j] + data[k] == 2020:
                print(data[i] * data[j] * data[k])