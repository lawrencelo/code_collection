import sys

def timeConversion(s):
    # Complete this function
    parseStringList=s.split(':')
    Hour = parseStringList[0]
    Minute = parseStringList[1]
    Second = parseStringList[2][0:2]

    if parseStringList[2][2:4] == 'AM':
        Hour = str(int(Hour) % 12)

    if parseStringList[2][2:4] == 'PM':
        if Hour != "12":
            Hour = str(int(Hour)+12)

    if int(Hour) < 10:
        Hour = '0' + Hour
    #print(Hour,Minute,Second,sep=':')
    TimeIn24 = "%s:%s:%s" % (Hour,Minute,Second)
    return TimeIn24


s = input().strip()
result = timeConversion(s)
print(result)