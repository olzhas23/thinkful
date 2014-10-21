'''READ SPECS:
REQUESTS:

Requests takes all of the work out of Python HTTP/1.1 — making your integration with web services seamless. There’s no need to manually add query strings to your URLs, or to form-encode your POST data.
Keep-alive and HTTP connection pooling are 100% automatic, powered by urllib3, which is embedded within Requests.
http://docs.python-requests.org/en/latest/

BEAUTIFUL SOUP:

is a Python library designed for quick turnaround projects like screen-scraping. Three features make it powerful:

1. Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree: a toolkit for dissecting a document and extracting what you need. It doesn't take much code to write an application
2. Beautiful Soup automatically converts incoming documents to Unicode and outgoing documents to UTF-8. You don't have to think about encodings, unless the document doesn't specify an encoding and Beautiful Soup can't detect one. Then you just have to specify the original encoding.
3. Beautiful Soup sits on top of popular Python parsers like lxml and html5lib, allowing you to try out different parsing strategies or trade speed for flexibility.
http://www.crummy.com/software/BeautifulSoup/'''
import requests
from bs4 import BeautifulSoup

def page_crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = "http://any" + str(page)
        source_code = requests.get(url) 
        code = source_code.text# here you get just the code
        
        var = BeautifulSoup(code) 
        for link in var.findAll('a', {'class': 'item-name'}): # here you have to specify what do you want to get like class, item-name etc.  look into the source
            href = "http://any" + link.get('href')
            title = link.string  # just the text, not the HTML
            print(href)
            print(title)
            # here you will just get data items like href, title etc
        page += 1  # here you will need to specify depth and steps


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    code = source_code.text
    var = BeautifulSoup(code)
    # if you want to gather information from that page
    for item_name in var.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    # if you want to gather links for a web crawler
    for link in var.findAll('a'):
        href = "any url" + link.get('href')
        print(href)


page_crawler(1)