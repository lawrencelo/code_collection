import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positiveNumbers = 0
negativeNumbers = 0
zeroNumbers = 0

for i in range(0,n):
    if arr[i] ==0:
        zeroNumbers += 1
    elif arr[i] > 0:
        positiveNumbers += 1
    elif arr[i] < 0:
        negativeNumbers += 1

print("{0:.6f}".format(positiveNumbers/n))
print("{0:.6f}".format(negativeNumbers/n))
print("{0:.6f}".format(zeroNumbers/n))

