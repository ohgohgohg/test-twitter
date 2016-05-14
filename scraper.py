# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

###############################################################################
# Twitter srcaper for the hashtag #bbcsms.
# https://github.com/aburan28/scrape10_twitter_scraper_4/blob/master/scraper.py
###############################################################################

import scraperwiki
import json as simplejson

# retrieve a page
base_url = 'http://search.twitter.com/search.json?q='
q = 'microphone'
options = '&rpp=100&page='
page = 1
import collections
cnt = collections.Counter()
cnt['I'] += 1

while 1:
    q = cnt.popitem()
    try:
        url = base_url + q + options + str(page)
        html = scraperwiki.scrape(url)
        #print html
        soup = simplejson.loads(html)
        for result in soup['results']:
            data = {}
            data['id'] = result['id']
            data['text'] = result['text']
            for word in data['text']:
                cnt[word] += 1 
                
            data['from_user'] = result['from_user']
            # save records to the datastore
            scraperwiki.datastore.save(["id"], data) 
        page = page + 1
    except:
        print str(page) + ' pages scraped'
        break
        
    
