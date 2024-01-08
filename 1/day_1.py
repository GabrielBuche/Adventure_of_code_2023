import re;

with open('data.in') as file:
    content = [i for i in file.read().strip().split('\n')]

arrayConcat = []
    
for calibrationValue in content:
    data = re.findall(r'\d', calibrationValue)
    concatNumbers = data[0] + data[len(data) - 1]
    arrayConcat.append(int(concatNumbers))
    
sumArray = sum(arrayConcat)

print(sumArray)