from pathlib import Path
import math
path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day5.txt'

dataIO = open(file, 'r')
dataLines = dataIO.readlines()
data = [x.rstrip('\n') for x in dataLines]

def determineRow(string):
    lb = 0
    ub = 127
    for s in string:
        split = (ub - lb) / 2
        if s == 'F':
            ub = lb + math.floor(split)
        else:
            lb = lb + math.ceil(split)
    return lb

def determineColumn(string):
    lb = 0
    ub = 7
    for s in string:
        split = (ub - lb) / 2
        if s == 'L':
            ub = lb + math.floor(split)
        else:
            lb = lb + math.ceil(split)
    return lb


a = determineRow('FBFBBFF')
print(a)
b = determineColumn('LRL')
print(b)

max_id = 0
ids = []
for line in data:
    row = determineRow(line[0:7])
    column = determineColumn(line[7:10])
    seatID = row * 8 + column
    max_id = max(max_id, seatID)
    ids.append(seatID)
    print(line + ': row ' + str(row) + ', column ' + str(column) + ', seat ID ' + str(seatID))
    
print(max_id)
sorted_ids = sorted(ids)
missing = [x for x in range(sorted_ids[0], sorted_ids[-1] + 1) if x not in sorted_ids]
print(missing)