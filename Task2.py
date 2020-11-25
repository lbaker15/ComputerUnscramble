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
def myMax(maxInitial, maxNumber, mapLength):
    max = maxInitial
    num = maxNumber
    for i in range(mapLength):
        value = calls[i][3]
        if int(value) > int(max):
            max = int(value)
            num = calls[i][0]
    return num, max
ans = myMax(calls[0][3], calls[0][1], len(calls))
print(ans[0], " spent the longest time,", ans[1], "seconds, on the phone in September 2016.")

"""
Worst-Case Big-O Notation:
O(n) as the function loops the input, meaning that complexity increases as the size of the size 
of the input increases.
"""