from pathlib import Path



path = Path("C:/Users/daan_/GitHub/AdventOfCode/Data")
file = path / 'day2.txt'

dataIO = open(file, 'r')
dataLines = dataIO.readlines()
data = [x.rstrip('\n') for x in dataLines]
data = [string.split(':') for string in data]
valid = 0
for i in range(len(data)):
    policy = data[i][0]
    bounds = policy.split(' ')[0].split('-')
    char = policy.split(' ')[1]
    password = data[i][1][1:]
    if int(bounds[0]) <= password.count(char, 0, len(password)) <= int(bounds[1]):
        valid += 1
        
print(valid)

valid = 0
for i in range(len(data)):
    check = 0
    policy = data[i][0]
    bounds = policy.split(' ')[0].split('-')
    char = policy.split(' ')[1]
    password = data[i][1][1:]
    if password[int(bounds[0]) - 1] == char:
        check += 1
    if password[int(bounds[1]) - 1] == char:
        check += 1
    if check == 1:
        valid += 1
print(valid)