from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Lucille.html"
for i in range(1,10):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
cnt = 0
for tag in tags:
    print(tag.get('href', None))
    cnt = cnt + 1
    if (cnt==18):
        url = tag.get('href', None)
        print(i,":",url)

