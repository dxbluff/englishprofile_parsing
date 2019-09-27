import requests, random
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

def getWord(url):
    page = requests.get(url, auth=('englishprofile', 'vocabulary'))
    result = page.text
    
    word = result.split("""<h1 class="hw" resource="us" query="yes">""")[1].split("</h1")[0]
    defenition = result.split("""<span class="def" resource="us" query="yes"><span> </span>""")[1].split("</span>")[0]
     
    pair = {word: defenition}
    print(pair)
    return pair
 
def getListOfWordsfromLink(links):
    words = []
    for i in links:
        words.append(getWord(i))
    return words

def getlinks(url):
    result = []
    for i in range(1,9):
        links = getLinksTo100Words(url + str(i))    
        links.pop(0)
        result += links
    return result

def saveToFile(words):
    f = open("a1_us.txt", 'w', encoding='utf8')
    for i in words:
        f.write(list(i.items())[0][0])
        f.write(" - ")
        f.write(list(i.items())[0][1])
        # print(i)
        # f.write(str(i))
        f.write("\n")
    f.close()


links = getlinks("""http://vocabulary.englishprofile.org/dictionary/search/us/?pageSize=100&q=&wl=301&p=""")
words = getListOfWordsfromLink(links)

random.shuffle(words)
random.shuffle(words)
            
saveToFile(words)
    
    





