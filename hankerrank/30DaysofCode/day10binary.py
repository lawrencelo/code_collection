import sys


n = int(input().strip())

binaryString = list(bin(n)[2:])

count = 0
biggestCount = 0
#print (binaryString)

for i in range(0, len(binaryString)):
    #print(binaryString[i])
    if binaryString[i] == str(1):
        count += 1
        if count > biggestCount:
            biggestCount = count
    else:
        count = 0

print (biggestCount)