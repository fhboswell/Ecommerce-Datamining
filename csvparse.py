with open("/Users/henryboswell/Desktop/Pants/zarapants.csv") as f:
    content = f.readlines()


print content[0].split(',')[5].replace('"', '')

for item in content:
	print item.split(',')[5].replace('"', '')