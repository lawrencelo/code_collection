import sys

def aVeryBigSum(n, ar):
    # Complete this function
    sum = 0
    print("n ", n, end="\n")
    for i in range(0,n):
        print("i ", i, end="\n")
        sum += ar[i]
    return sum
# 5
# 1000000001 1000000002 1000000003 1000000004 1000000005
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)