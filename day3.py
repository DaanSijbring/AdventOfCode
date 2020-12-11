from pathlib import Path
import math
import numpy
path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day3.txt'

dataIO = open(file, 'r')
dataLines = dataIO.readlines()
data = [x.rstrip('\n') for x in dataLines]
data = [list(line) for line in data]

x = 0
trees = 0
for i in range(len(data)):
    if data[i][x % len(data[i])] == '#': trees += 1
    x += 3
print(trees)

treesTotal = {}
slopes = [[1, 1], [3, 1], [5,1], [7,1], [1,2]]
for jumps in slopes:
    x = 0
    y = 0
    trees = 0
    for i in range(math.floor(len(data) / jumps[1])):
        if data[y][x % len(data[y])] == '#': trees += 1
        x += jumps[0]
        y += jumps[1]
    treesTotal[(jumps[0], jumps[1])] = trees
sumTrees = numpy.prod([treesTotal[jumps] for jumps in treesTotal])
print(sumTrees)