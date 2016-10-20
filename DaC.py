from bs4 import BeautifulSoup
import requests
import string
import wikipedia
from google import search

def printAll(listName):
    for item in listName:
        print "- " + item[0] + ": " + item[1]
        print("")

def writeTerms(termData):
    f = open("terms.md","w")
    f.write((u"# Define and Conquer  \n").encode('UTF-8'))
    for item in termData:
        # item[0] = term name
        # item[1] = term definition
        f.write((u"**"+unicode(item[0])+u"**: ").encode('UTF-8'))
        f.write((unicode(item[1])+u"  \n\n").encode('UTF-8'))
    f.close()

def readTerms():
    # read the terms from the file: terms.txt
    terms = [line.rstrip('\n') for line in open('terms.txt')]
    return terms

def wikiSearch(searchString):
    urls = []
    for url in search(searchString + " site:wikipedia.org", stop=10):
        # we only want three urls.
        # 'relevant' wikipedia sub-urls have '?sa=X&ved=' in them... filter that
        if (len(urls) < 3) and ("?sa=X&ved=" not in url):
            urls.append(url)

    return urls

def searchTerm(term):
    # using the wikipedia module, print out the first 5 sentences of the article
    # introduction / summary.
    try:
        summary = wikipedia.summary(term, sentences=2)
    except:
        try:
            newTitle = wikiSearch(term)[0].rsplit("/wiki/",1)[1]
            print("Couldn't find " + term + "... Checking /wiki/"+newTitle)
            summary = wikipedia.summary(newTitle, sentences=1)
        except:
            try:
                print("Still didn't work for some reason. Using page's .content")
                newTitle = wikiSearch(term)[0].rsplit("/wiki/",1)[1]
                summary = wikipedia.WikipediaPage(newTitle).content.split(".")[0]+"."
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

writeTerms(definitions)
# ==========================   END MAIN FUNCTION   =============================
# ===========================   BEGIN DEBUGGING   ==============================
# ============================   END DEBUGGING   ===============================
