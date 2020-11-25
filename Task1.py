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


def task1(texts):
    numbers = []
    for i in range(len(texts)):
        if texts[i][0]:
            if not texts[i][0] in numbers:
                numbers.append(texts[i][0])
        if texts[i][1]:
            if not texts[i][1] in numbers:
                numbers.append(texts[i][1])
        if i < len(calls):
            if calls[i][0]:
                if not calls[i][0] in numbers:
                    numbers.append(calls[i][0])
            if calls[i][1]:
                if not calls[i][1] in numbers:
                    numbers.append(calls[i][1])
    return len(numbers)

print("There are ",task1(texts), " different telephone numbers in the records.")

"""
Worst-Case Big-O Notation:
Big O notation would be O(n) as the function loops the input meaning that complexity increases as the size of the size 
of the input increases.
"""
