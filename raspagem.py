from bs4 import BeautifulSoup
import requests


url= 'https://www.instagram.com'
resposta = requests.get(url)
conteudo_html= resposta.content

soup = BeautifulSoup(conteudo_html,
                     'html.parser')

links = soup.find_all('a')


for link in links:
    print("texto:{%s}, URL:{%s}"
    % (link.text, link.get('href')))
    
