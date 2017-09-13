import sys

def main():
    n = int(input().strip())
    phoneDict = {}
    for i in range(0,n):
        inputString = input().strip().split(' ')
        phoneDict[inputString[0]] = inputString[1]

    #print (phoneDict)

    for line in sys.stdin:
        key=line.strip()
        if key in phoneDict:
            print(key,"=",phoneDict[key],end='\n', sep="")
        else:
            print("Not found")

if __name__ == "__main__": main()