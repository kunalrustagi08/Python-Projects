# -*- coding: utf-8 -*-
import requests
from requests import get
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/page-1.html'

results = requests.get(url)

soup = BeautifulSoup(results.text, 'html.parser')
print(soup.prettify())

book_title = []
product_price = []
star_rating = []

book_div = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
print(book_div)

for container in book_div:
    name = container.article.h3.a['title']
    book_title.append(name)

    price = container.article.find('div', class_='product_price').p.text
    product_price.append(price)

    rating = container.article.p['class'][-1]
    star_rating.append(rating)

print(book_title)
print(product_price)
print(star_rating)

import pandas as pd

col_dict = {'title' : book_title, 'price' : product_price, 'rating' : star_rating}
book_store = pd.DataFrame(col_dict)

print(book_store.head())
print(book_store.dtypes)

number_mapping = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
book_store['rating'] = book_store.rating.apply(lambda x : number_mapping.get(x))

book_store['price'] = book_store['price'].apply(lambda x: float(x[2:]))

print(book_store.head())
print(book_store.dtypes)

book_store.to_csv('book_store.csv')
