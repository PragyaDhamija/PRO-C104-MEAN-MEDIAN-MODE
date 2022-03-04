import csv
with open('Project/heightWeight.csv', newline = '') as f:
    r= csv.reader(f) 
    fileData = list(r)
fileData.pop(0)

newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
    
n = len(newData)

newData.sort()
if n%2 == 0:
    median1 = float(newData[n//2]) 
    median2 = float(newData[n//2-1])
    median = (median1+median2)/2
else:
    median = newData[n//2]
print("Your required median for weight of 18 year olds is ==>" +str(median))