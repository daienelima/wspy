from re import T
from bs4 import BeautifulSoup
import requests
url = 'https://www.wattpad.com/1259494600-outsider-•-10-•"'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

html = result.content

soup = BeautifulSoup(html, 'html.parser')
test = soup.findAll('pre')

full_text=[]

for i in range(len(test)):
    full_text.append(test[i].get_text() + "\n\n") 

print(''.join(full_text))
#print(test)
