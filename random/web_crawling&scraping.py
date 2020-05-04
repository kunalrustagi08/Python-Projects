import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import time
import random

pages = np.arange(1,51,1)

book_title = []
star_rating = []
product_price = []

for page in pages:
    time.sleep(random.randint(1,10))
    
    url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
    results = requests.get(url)
    soup = BeautifulSoup(results.text, 'html.parser')

    book_div = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

    for container in book_div:
        title = container.article.h3.a['title']
        book_title.append(title)

        price = container.article.find('div', class_='product_price').p.text
        product_price.append(price)

        rating = container.article.p['class'][-1]
        star_rating.append(rating)


import pandas as pd
col_dict = {'title':book_title, 'price':product_price, 'rating':star_rating}
book_store = pd.DataFrame(col_dict)

print(book_store.head())
print(book_store.dtypes)

book_store['price'] = book_store['price'].apply(lambda x : float(x[2:]))

number_mapping = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
book_store['rating'] = book_store['rating'].apply(lambda x : number_mapping.get(x))

print(book_store.head())
print(book_store.dtypes)

book_store.to_csv('book_store.csv')
