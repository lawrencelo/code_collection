import sys

def processString(inputString):
    oddStringList = []
    evenStringList =[]

    for i in range(0,len(inputString)):
        #print("", inputString[i], end='')
        if i%2:
            evenStringList.append(inputString[i])
        else:
            oddStringList.append(inputString[i])

    for i in range(0,len(oddStringList)):
        print(oddStringList[i], end='')

    print(" ", end='')

    for i in range(0,len(evenStringList)):
        print(evenStringList[i], end='')

def main():
    n = int(input().strip())
    for i in range(0,n):
        inputString = input().strip()
        processString(inputString)
        print(" ")


if __name__ == "__main__": main()