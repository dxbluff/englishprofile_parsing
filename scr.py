import requests
from requests.auth import HTTPBasicAuth


def getLinksTo100Words(url):
    page = requests.get(url, auth=('englishprofile', 'vocabulary'))
    result = page.text

    result=result.split("<ul>")[1]
    result=result.split("</ul>")[0]

    result = result.split("<li><a href=\"")
    result2 = []
     
    for i in result:
        i = i.split("\"><span", 1)[0]
        result2.append("http://vocabulary.englishprofile.org" + i)
    return result2

links = getLinksTo100Words("http://vocabulary.englishprofile.org/dictionary/search/uk/?pageSize=100&q=&wl=301&p=1")






