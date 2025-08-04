import requests, os, bs4    
url='https://pt-br.facebook.com'
os.makedirs('gigihtok', exist_ok=True)
while not url.endswith('#'):
    print('dowloading page %s...'% url)
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
print(soup)