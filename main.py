
import webbrowser
import requests
from playsound import playsound
import vlc
import time

# zad3

# Za pomocą playsound
# playsound("D:\PycharmProjects\PPY10_03\yippee.mp3")
##I za pomocą vlc
# p = vlc.MediaPlayer("D:\PycharmProjects\PPY10_03\yippee.mp3")
# p.play()
# time.sleep(3)
# p.stop()

# Zad4
pageUrl = 'https://github.com'
date = 20150101

pageUrl = input("podaj adres strony\n")

print("Podaj trzy daty, z których wybrać snapshoty\n")
for x in range(3):
    date = input("podaj date np. 20230130\n")

    url = "http://archive.org/wayback/available?url=" + pageUrl + "&timestamp=" + str(date)
    response = requests.get(url)
    d = response.json()
    print(d ,"\n")
    page = d["archived_snapshots"]["closest"]["url"]
    webbrowser.open(page)
print("Trzy strony znalezione!")
