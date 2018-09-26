#!/usr/bin/python3

#########################################################################
# A script to take the new items feed from Zotero and create a new feed
# that has the document's actual URL as the item URL, instead of a Zotero
# internal URL. fbarton@alwaysdata.net
#########################################################################

import feedparser
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator

rss = feedparser.parse('https://api.zotero.org/users/76164/items/top?start=0&limit=25&format=atom&v=1')

# get the info from the 'content' section of the RSS entry and pass it through bs4 so the tags are recognised as such
# need to change this so it iterates through all new additions to the feed
stuff = str(rss.entries[0]['content'])
soup = BeautifulSoup(stuff, 'lxml')

# selects the child elements of the two table rows we are interested in
author_tag = soup.select(".creator > td")
url_tag = soup.select(".url > td")

# author_tag and url_tag are created as lists by bs4.select, not strings, so you can't just say
# author = author_tag.get_text()
# as this throws an error: get_text can't operate on lists. So you have to iterate the list even though there is only one item in the list.
for a in author_tag:
	author = a.get_text()
for u in url_tag:
	url = u.get_text()

print("Author: " + author + ";\n" + "URL: " + url)

# next steps are to create new feed items using author and url and get them
# appended to the new feed, using feedgen (perhaps)
