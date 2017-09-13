import sys

def factorial(n):
    # Complete this function
    number = 1
    for i in range(0,n):
        number *= i+1
    return number

if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)