import bs4
import requests

url ="http://jadwalsholat.pkpu.or.id/monthly.php?id=9"
response = requests.get(url)
content = bs4.BeautifulSoup(response.text, "html.parser")

data = content.find_all("tr", "table_highlight")
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat["shubuh"] = d.get_text()
    elif i == 2:
        sholat["dzuhur"] = d.get_text()
    elif i == 3:
        sholat["ashar"] = d.get_text()
    elif i == 4:
        sholat["maghrib"] = d.get_text()
    else:
        sholat["isya"] = d.get_text()
    i += 1
print(sholat)



