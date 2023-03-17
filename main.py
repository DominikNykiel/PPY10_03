

import webbrowser
import requests


#Zad4
#pageUrl = 'https://github.com'
#date = 20150101

pageUrl = input("podaj adres strony")

print("Podaj trzy daty, z których wybrać snapshoty")
for x in range(3):
    date = input("podaj date np. 20230130")

    url = "http://archive.org/wayback/available?url=" + pageUrl + "&timestamp=" + str(date)
    response = requests.get(url)
    d = response.json()
    print(d)
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
print("Trzy strony znalezione!")


