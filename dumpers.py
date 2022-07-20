import requests
from lxml import html

def dumpCases():
    URL = "https://csgostash.com/containers/skin-cases"

    p = requests.get(URL)
    tree = html.fromstring(p.content)
    divs = tree.xpath('//*[@class="container main-content"]//div[@class="row"]')
    i =  0
    for div in divs:
        i += 1
        if i == 6:
            break

        href = div.xpath('.//a/@href')

    links =[]
    try:
        i = 0
        while True:
            i += 2
            links.append(href[i])
    except:
        links.remove("https://csgostash.com/case/292/X-Ray-P250-Package")
        return links

def dumpCaseSkins(link):
    p = requests.get(link)
    tree = html.fromstring(p.content)
 
    divs = tree.xpath('//*[@class="container main-content"]//div[@class="row"]')

    i = 0
    huntsman = link == "https://csgostash.com/case/17/Huntsman-Weapon-Case"
    
    for div in divs:
        i += 1
        if i == 8 and not huntsman:
            break
        if i == 9 and huntsman:
            break
        text = div.xpath('.//a/text()')

    skins = []
    for entry in text:
        if " Skin & Price Details" in entry:
            skins.append(entry.removesuffix(" Skin & Price Details"))

    return skins

def dumpCasePicture(link):
    a = link.split("/")[-1]
    p = requests.get(link)
    xhtml = html.fromstring(p.content)
    imageUrl = xhtml.xpath(f'//img[@alt="{a.replace("-", " ")}"]/@src')
    return imageUrl[1]

for case in dumpCases():
    print(dumpCasePicture(case))