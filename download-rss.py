import urllib.request

#馬鳥速報
url = "http://blog.livedoor.jp/umadori0726/index.rdf"
res = urllib.request.urlopen(url)
data = res.read()

text = data.decode("utf-8")
print(text)
