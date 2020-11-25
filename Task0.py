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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def cases(texts, calls):
    first = texts[0]
    last = calls[len(calls) - 1]
    print("First record of texts, ", first[0], " texts ", first[1], " at ", first[2])
    print("Last record of calls, ", last[0], "calls ", last[1], " at time ",
          last[2], " lasting ", last[3], " seconds")

cases(texts, calls)

"""
Worst-Case Big-O Notation:
Big O notation would be O(1) as both the declarations and printed messages only need to run once despite whatever input 
is passed into the function.
I implemented a constant notation so the runtime doesn't change despite the input
"""