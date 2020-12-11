from pathlib import Path
import re
path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day4.txt'

dataIO = open(file, 'r')
dataLines = dataIO.readlines()
data = [x.rstrip('\n') for x in dataLines]
newData = []
runningPassport = ''
for line in data:
    if not line: 
        newData.append(runningPassport[:-1])
        runningPassport = ''
        continue
    else:
        runningPassport += line + ' '
newData.append(runningPassport[:-1])
newData = [[field.split(':') for field in passport.split(' ')] for passport in newData]

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valids = 0
for passport in newData:
    fields = [entry[0] for entry in passport]
    if 'cid' in set(fields): fields.remove('cid')
    if len(fields) == 7: valids += 1
    
print(valids)

valids = 0
for passport in newData:
    fields = [entry[0] for entry in passport]
    if 'cid' in set(fields): fields.remove('cid')
    if not len(fields) == 7: continue
    passDict = {}
    for field in passport:
        passDict[field[0]] = field[1]
    if not 1920 <= int(passDict['byr']) <= 2002: continue
    if not 2010 <= int(passDict['iyr']) <= 2020: continue
    if not 2020 <= int(passDict['eyr']) <= 2030: continue
    height = re.split('(\d+)',passDict['hgt'])
    if height[2] == 'cm':
        if not 150 <= int(height[1]) <= 193: continue
    elif height[2] == 'in':
        if not 59 <= int(height[1]) <= 76: continue
    else:
        continue
    if not bool(re.match('^#([a-f0-9]{6})$', passDict['hcl'])): continue
    if not passDict['ecl'] in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']): continue
    if not len(passDict['pid']) == 9: continue
    if not passDict['pid'].isnumeric(): continue
    print(passDict['pid'])
    #print(passDict)
    valids += 1
print(valids)