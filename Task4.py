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

arr = []
def receivedCalls(toMap):
    for i in range(len(toMap)):
        if calls[i][0] not in calls[i][1]:
            if calls[i][0] not in arr:
                arr.append(calls[i][0])

def texting(texts):
    for i in range(len(texts)):
        if texts[i][0] in arr:
            arr.remove(texts[i][0])
        if texts[i][1] in arr:
            arr.remove(texts[i][1])

receivedCalls(calls)
texting(texts)
print("These numbers could be telemarketers:")
for x in sorted(arr):
    print(x)

"""
Worst-Case Big-O Notation:
Both functions are O(n) as they loop the input, meaning that complexity increases as the size of the size 
of the input increases.
"""
