import urllib.request
from bs4 import BeautifulSoup

#馬鳥速報
url = "http://blog.livedoor.jp/umadori0726/index.rdf"
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res, "html.parser")



for item in soup.find_all("item"):
    print(item.find("title").string)
    print(item.attrs['rdf:about'])
    print(item.find("dc:date").string)

