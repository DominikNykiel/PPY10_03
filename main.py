# This is a sample Python script.

import webbrowser
import requests

#pageUrl = 'https://github.com'
#date = 20150101

pageUrl = input("podaj adres strony")
date = input("podaj date np. 20230130")
url = 'http://archive.org/wayback/available?url=' + pageUrl + '&timestamp' + str(date)
response = requests.get(url)
d = response.json()
print(d)
page = d["archived_snapshots"]["closest"]["url"]

webbrowser.open(pageUrl)
