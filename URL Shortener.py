# Shortener the Longer URL using build in Library files
# pyshorteners
# pyperclip

import pyshorteners

def shortenerurl(url):
    shorturl = pyshorteners.Shortener()
    print(shorturl.tinyurl.short(url))


url = input("Enter the URL to Shortening: ")
shortenerurl(url)
