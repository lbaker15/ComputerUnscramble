"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketers():
    callers = set()
    for i in range(len(calls)):
        callers.add(calls[i][0])
    for i in range(len(calls)):
        if calls[i][1] in callers:
            callers.remove(calls[i][1])
    for text in texts:
        if text[0] in callers:
            callers.remove(text[0])
        if text[1] in callers:
            callers.remove(text[1])
    return sorted(callers)
callers = telemarketers()
print("These numbers could be telemarketers: ")
for caller in callers:
    print(caller)

