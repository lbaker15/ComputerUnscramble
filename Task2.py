"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
"""
def myMax(startReceivingNum, startSeconds, mapLength):
    max = startSeconds
    num = startReceivingNum
    for i in range(mapLength):
        value = calls[i][3]
        if int(value) > int(max):
            max = int(value)
            num = calls[i][0]
    return num
ans = myMax(calls[0][1], calls[0][3], len(calls))
def seconds():
    count = 0
    for x in calls:
        if x[0] == ans:
            count += int(x[3])
        if x[1] == ans:
            count += int(x[3])
    return count
countNum = seconds()
print(ans, " spent the longest time,", countNum, "seconds, on the phone in September 2016.")
"""
def dialled(mapLength):
    dict = {}
    for i in range(mapLength):
        if calls[i][0] in dict:
            getValue = dict.get(calls[i][0])
            updateTo = int(getValue) + int(calls[i][3])
            dict.update({calls[i][0]: updateTo})
        else:
            dict.update({calls[i][0]: calls[i][3]})
    return dict
dialledValue = dialled(len(calls))

def received(value):
    updatedDict = value
    for i in range(len(calls)):
        if calls[i][1] in updatedDict:
            oldValue = updatedDict.get(calls[i][1])
            updateTo = int(oldValue) + int(calls[i][3])
            updatedDict.update({calls[i][1]: updateTo})
        else:
            updatedDict.update({calls[i][1]: calls[i][3]})
    return updatedDict
updatedValue = received(dialledValue)

def highest():
    max = 0
    for value in updatedValue:
        if int(updatedValue[value]) > int(max):
            max = updatedValue[value]
    for value in updatedValue:
        if max == updatedValue[value]:
            number = value
    return number, max
finalAnswer = highest()
print(finalAnswer[0], finalAnswer[1])

