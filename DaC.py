from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import wikipedia

lines = [line.rstrip('\n') for line in open('terms2.txt')]
notFound = []
paragraphs = []

arrayMax = len(lines)


def summarize(x):
    try:
        while x in xrange(0,arrayMax):
            print lines[x]
            print wikipedia.summary(lines[x], sentences=5)
            print('\n\n')
            x+=1
    except:
        if lines:
            print(lines[x] + " was not able to be found.\n\n")
            notFound.append(lines[x])
            lines.pop(x)
            print lines
        if x != arrayMax:
            summarize(x)

if lines:
    summarize(0)

print("The list of indentified terms includes:\n" + str(notFound))
