# This scrapes em-list-unicode and saves the emojis as ong files
from bs4 import BeautifulSoup
import requests
import base64

with open('./rawdata/em-list-unicode-v12.1.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

for tr in soup.find_all('tr'):
	if(tr.find('td',class_='rchars')!=None):
		emoji_name = tr.find('td',class_='name').text

		print(emoji_name)

		td = tr.find_all('td', class_='andr')[1]
	
		imgdata = base64.b64decode(td.img['src'][22:])

		with open("./dataset/"+emoji_name, 'wb') as f:
			f.write(imgdata)