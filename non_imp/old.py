'''
import requests
from bs4 import BeautifulSoup

ticker = 'NIFTY_50'
exchange = 'INDEXNSE'
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

x = [1]
y = list()

for i in range(100):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    class1 = 'YMlKec'

    y.append(float(soup.find(class_=class1).text.replace(',', '')))
    x.append(x[-1] + 1)

print(x, y)
'''
