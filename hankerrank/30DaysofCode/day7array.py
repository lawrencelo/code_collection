import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(0,len(arr)):
    print(arr[len(arr)-i-1], "", end='')