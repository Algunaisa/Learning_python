###
# https://realpython.com/python-web-scraping-practical-introduction/
###

from urllib.request import urlopen
# for Regular expressions:
import re

def printSlash():
    print("\n-------------------------------------------------------------\n\n")

def getHTML(god):
    url = "http://olympus.realpython.org/profiles/"+god
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print("\tHTML: \n",html)
    return html

def getTitleByLen(god):
    html = getHTML(god)

    title_index = html.find("<title>")
    #14
    start_index = title_index + len("<title>")
    #21
    end_index = html.find("</title>")
    #39
    title = html[start_index:end_index]
    #'Profile: Aphrodite'
    print("\tTitle: \n",title)
    return title

def getTitleByRe(god):
    html = getHTML(god)

    pattern = "<title.*?>.*?</title.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Remove HTML tags
    print("\tTitle: \n",title)
    return title

#poseidon
#aphrodite
#dionysus

title = getTitleByLen("aphrodite")

printSlash()

title = getTitleByRe("poseidon")

printSlash()

title = getTitleByRe("dionysus")

printSlash()

