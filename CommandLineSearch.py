import requests
import bs4, webbrowser, sys

print('Wanna find something?')
query = input()
print('Search in progress...')
page = requests.get('https://www.google.co.in/search?q=%s' %query)
soup = bs4.BeautifulSoup(page.text)
element = soup.select('.r a')

# open first three links
for i in range(3):
    webbrowser.get("/usr/bin/google-chrome %s").open('https://google.com'+element[i].get('href'))
