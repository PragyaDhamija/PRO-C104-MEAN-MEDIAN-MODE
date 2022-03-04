import csv
with open('Project/heightWeight.csv', newline = '') as f:
    r= csv.reader(f) 
    fileData = list(r)
fileData.pop(0)

newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append( float(num) )
    
n = len(newData)
sum = 0
for i in newData:
    sum+=i
mean = sum/n
print("Your required mean for weight of 18 year olds is ==>" + str(mean))