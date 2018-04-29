# -*- coding: utf-8 -*-
from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

browser = webdriver.Chrome()



with open("/Users/henryboswell/Desktop/Pants/zarapantsreduced.csv") as f:
    content = f.readlines()


print content[0].split(',')[5].replace('"', '')

overall = 216
for item in content:
	overall = overall + 1
	print item.split(',')[5].replace('"', '')
	url = item.split(',')[5].replace('"', '')


	browser.get(url)  

	html_source = browser.page_source  
	soup = BeautifulSoup(html_source, 'html.parser')

	#allImgZoom = soup.findAll('img')
	#for image in allImgZoom:
	    #print image source
	    #print image['src']

	allImgZoom = soup.find_all(class_='_seoImg')

	print(len(allImgZoom))
	#allImgZoom = soup.findAll('img')
	text = soup.find_all(class_='description')[0]
	name = soup.find_all(class_='product-name')[0]
	color = soup.find_all(class_='_colorName')[0]
	i = 0
	for image in allImgZoom:
	    #print image source
	    i = i + 1
	    print image['href']
	    img_data = requests.get("http:" + image['href']).content
	    with open("/Users/henryboswell/Desktop/Pants/img/" + str(overall) + "pants" +str(i) + '.jpg', 'wb') as handler:
	    	handler.write(img_data)
	    file = open('/Users/henryboswell/Desktop/Pants/desc1/' + str(overall) + 'pants' + str(i)+ ".jpg.txt",'w') 
	    file.write(str(text))
	    file.write(str(color.text)) 
	    file.close()
	    file = open('/Users/henryboswell/Desktop/Pants/desc2/' + str(overall) + 'pants' + str(i)+ ".jpg.txt",'w') 
	    file.write(str(name.text) + "\n") 
	    file.write(str(color.text)) 
	    file.close()  


#link = browser.find_element_by_link_text('Next product').click()

browser.quit()