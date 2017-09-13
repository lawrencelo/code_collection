import sys

#3
#11 2 4
#4 5 6
#10 8 -12

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

#print(abs(a[0][0]+a[1][1]+a[2][2]-(a[0][2]+a[1][1]+a[2][0])))

diag1 = 0
diag2 = 0
for i in range(0, n):
    diag1 += a[i][i]
    diag2 += a[i][n - i - 1]

print(abs(diag1 - diag2))