import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

width = 6
height = 6
maxHourglassSum = -99999999
for i in range(0,height-2):
    for j in range(0,width-2):
        # hourglass sum
        hourglassSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if hourglassSum > maxHourglassSum:
            maxHourglassSum = hourglassSum

print(maxHourglassSum)
