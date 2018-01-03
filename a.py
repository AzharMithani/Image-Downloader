import requests
from bs4 import BeautifulSoup

payload = {'q': 'google',  # enter your query here
           'source': 'lnms', 'tbm': 'isch'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/59.0.3071.86 Safari/537.36'}
s = requests.get('http://www.google.com/search', headers=headers, params=payload).text
soup = BeautifulSoup(s, 'html.parser')
i = 0
for link in soup.find_all('img'):
    try:
        r = requests.get(str(link.get('data-src')), headers=headers)
        i = i + 1
        with open(payload['q'] + str(i) + ".png", 'wb') as f:
            f.write(r.content)
            print(i)
    except Exception as e:
        pass




