import re
import requests

with open('dataset_3378_3.txt','r') as inf:
	file=requests.get(inf.readline().strip())
	file="https://stepic.org/media/attachments/course67/3.6.3/" + file.text
	print(file)

s=0
while True:
#	with open(file, 'r') as all:
#	file = requests.get(all.readline().strip())
	s+=1
	file = requests.get(file)
	text=file.text
	file="https://stepic.org/media/attachments/course67/3.6.3/" + file.text
	file2=text.split(' ')
	print(s, file2[0])
	if file2[0] == "We":
		print(text)
		break