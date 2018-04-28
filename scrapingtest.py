import requests

page = requests.get("https://www.zara.com/us/en/cropped-palazzo-trousers-p01564450.html?v1=6157131&v2=719514")
page

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

#print(list(soup.children))

[type(item) for item in list(soup.children)]
#print(soup.findAll('img'))


allImgZoom = soup.find_all(class_="_img-seo")

print(allImgZoom)

print("\n")



print(len(allImgZoom))
allImgZoom = soup.findAll('img')
for image in allImgZoom:
    #print image source
    print image['src']
    #print alternate text
    print image['alt']