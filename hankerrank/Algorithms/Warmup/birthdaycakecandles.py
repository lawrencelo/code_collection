import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    tallest=0
    tallestNumbers=0
    for i in range(0,len(ar)):
        if ar[i] > tallest:
            tallest = ar[i]
            tallestNumbers=1
        elif ar[i] == tallest:
            tallestNumbers += 1

    return tallestNumbers


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)