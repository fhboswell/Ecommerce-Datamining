from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('https://www.zara.com/us/en/cropped-palazzo-trousers-p01564450.html?v1=6157131&v2=719514')  
html_source = browser.page_source  
browser.quit()

soup = BeautifulSoup(html_source, 'html.parser')
#print(soup.prettify())

#print(list(soup.children))


#print(soup.findAll('img'))


allImgZoom = soup.find_all(class_='description')

comments = soup.findAll('img',{'class':'_img-zoom'})  
print comments

print(allImgZoom)

print("\n")



print(len(allImgZoom))
#allImgZoom = soup.findAll('img')
#for image in allImgZoom:
    #print image source
    #print image['src']

allImgZoom = soup.find_all(class_='_seoImg')

print(len(allImgZoom))
#allImgZoom = soup.findAll('img')
for image in allImgZoom:
    #print image source
    print image['href']

    allImgZoom = soup.find_all(class_='_seoImg')

print(len(allImgZoom))
#allImgZoom = soup.findAll('img')
for image in allImgZoom:
    #print image source
    image.get_text()