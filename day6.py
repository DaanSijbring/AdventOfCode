from pathlib import Path

path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day6.txt'

dataIO = open(file, 'r')
dataLines = dataIO.readlines()
data = [x.rstrip('\n') for x in dataLines]
newData = []
runningGroup = ''
for line in data:
    if not line: 
        newData.append(runningGroup)
        runningGroup = ''
        continue
    else:
        runningGroup += line
newData.append(runningGroup)

forms = [len(set(group)) for group in newData]
print(sum(forms))

groupData = []
group = []
for line in data:
    if not line:
        groupData.append(group)
        group = []
        continue
    else:
        group.append(set(line))
groupData.append(group)

forms = []
for group in groupData:
    result = group[0]
    for x in group[1:]:
        result.intersection_update(x)
    forms.append(len(result))
print(sum(forms))