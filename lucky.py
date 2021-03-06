#! python3
# lucky.py - Opens several Google search results.

import requests
import sys
import webbrowser
import bs4


print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup((res.text), "html5lib")

# Open a browser tab for each result.
link_elems = soup.select('.LC20lb DKV0Md a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))
