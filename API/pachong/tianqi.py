from bs4 import BeautifulSoup
import requests
url="http://www.weather.com.cn/weather1d/101110508.shtml"

resp = requests.get(url)
#print(resp.text)

#print(resp.content.decode('utf8'))

html = resp.content.decode('utf8')

soup = BeautifulSoup(html,'html.parser')
body = soup.body
data = body.find("div",{"id":"7d"})
ul = data.find("ul")
li = ul.find_all("li")
print(li)

for day in li:
        temp = []
        date=day.find_all("h1")
        temp.append(date)
        inf=day.find_all("p")
        temp.append(inf[0].string) 
        print(inf[0])

