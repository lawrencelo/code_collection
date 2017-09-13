import sys

arr = list(map(int, input().strip().split(' ')))

minSum=10000000000
maxSum=1

for i in range(0,len(arr)):
    #print(arr[i])
    totalSum=0
    for j in range(0,len(arr)):
        if i==j:
            continue
        else:
            totalSum += arr[j]

    if totalSum > maxSum:
        maxSum = totalSum
    if totalSum < minSum:
        minSum = totalSum

print(minSum, maxSum)