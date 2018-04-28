
import requests

img_data = requests.get("http://static.zara.net/photos/2018/V/0/2/p/1564/450/800/2/w/560/1564450800_6_1_1.jpg?ts=1524755942024").content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)