from bs4 import BeautifulSoup
import requests
import string
import wikipedia

def printAll(listName):
    for item in listName:
        print item[0] + ": " + item[1]
        print("\n")

def readTerms():
    # read the terms from the file: terms.txt
    terms = [line.rstrip('\n') for line in open('terms.txt')]
    return terms

def searchTerm(term):
    # using the wikipedia module, print out the first 5 sentences of the article
    # introduction / summary.
    try:
        summary = wikipedia.summary(term, sentences=5)
    except:
        summary = "Definition could not be found."
    return (term, summary)


# ============================   MAIN FUNCTION   ===============================
print("Beginning the search...")
definitions = []
terms = readTerms()
for term in terms:
    # search for the term and store its definition.
    definitions.append(searchTerm(term))

printAll(definitions)
# ==========================   END MAIN FUNCTION   =============================
