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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""
from operator import itemgetter, attrgetter

def filter(calls):
    arr = []
    substring = "(080)"
    for x in calls:
        if substring in x[0]:
            if x[1][0] == "(":
                code = x[1].split(")")[0] + ")"
            else:
                code = x[1][0] + x[1][1] + x[1][2]
            if not code in arr:
                arr.append(code)
    arr.sort()
    for x in arr:
        print(x)
print("The numbers called by people in Bangalore have codes:")
filter(calls)

"""
Worst-Case Big-O Notation:
O(2n) as the function loops the input and the then the array, the size of which is dependent 
on the input.
"""



"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def filter(calls):
    allCalls = []
    substring = "(080)"
    for x in calls:
        if substring in x[0]:
            allCalls.append(x[1])
    return allCalls

def percentage(ans):
    noCalls = len(ans)
    substring = "(080)"
    count = 0
    for x in ans:
        if substring in x:
            count += 1
    perc = count / noCalls * 100
    decPoint = str(round(perc, 2))
    print(decPoint + "% of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore")

ans = filter(calls)
percentage(ans)

"""
Worst-Case Big-O Notation:
Both functions are O(n) as they loop the input, meaning that complexity increases as the size of the size 
of the input increases.
"""