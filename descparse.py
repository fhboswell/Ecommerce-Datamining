with open("/Users/henryboswell/Desktop/Pants/alllabels.txt") as f:
    content = f.readlines()


f.close()

labels = []
for item in content:
	labels.append(item.strip('\n'))
print labels

import os
for f in os.listdir('/Users/henryboswell/Desktop/Pants/desc1/'):
	print f
	with open("/Users/henryboswell/Desktop/Pants/desc1/" + f) as file:
		data = file.readlines()
		print data
		dataLower = data[0].lower()

		file = open("/Users/henryboswell/Desktop/Pants/pantsdesc/" + f,'w') 

		for item in labels:
			if item in dataLower:
				file.write(item + "\n")
		file.close()

