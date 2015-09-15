from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import wikipedia

lines = [line.rstrip('\n') for line in open('terms2.txt')]
notFound = []
paragraphs = []

arrayMax = len(lines)
rangeMax = len(lines) - 1
finished = False
print(rangeMax)
print arrayMax


def summarize(x):
    try:
        while x in xrange(0,arrayMax):
            print lines[x]
            print wikipedia.summary(lines[x], sentences=5)
            print('\n\n')
            x+=1
            if x == rangeMax:
                finished = True
    except:
        if x != rangeMax:
            print(lines[x] + " was not able to be found.\n\n")
            notFound.append(lines[x])
            x+=1
            summarize(x)
        if x == rangeMax:
            finished = True

if arrayMax > 0 and finished != True:
    summarize(0)
    print("The list of unindentified terms includes:\n" + str(notFound))
else:
    print "Please enter some terms in terms2.txt"
