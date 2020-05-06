import requests
from bs4 import BeautifulSoup
import time 
import random
import numpy as np
from multiprocessing import Pool

url_list = []

pages = np.arange(1,51,1)

def generate_urls():
    for page in pages:
        url = 'http://books.toscrape.com/catalogue/page-' + str(page) + '.html'
        url_list.append(url)

def scrape_url(url):
    book_title = []
    star_rating = []
    product_price = []
    
    time.sleep(random.randint(5,15))
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

    return (book_title, product_price, star_rating)

generate_urls()
for i in url_list[:10]:
    print(i)

start = time.time()

p = Pool(10)
book_list = p.map(scrape_url, url_list)
p.terminate()
p.join()
end = time.time()
print('It took', (end-start), 'seconds')

titles = [bk for tupl in book_list for bk in tupl[0]]
prices = [price for tupl in book_list for price in tupl[1]]
ratings = [star for tupl in book_list for star in tupl[2]]

import pandas as pd
col_dict = {'title':titles, 'price':prices, 'rating':ratings}
book_store = pd.DataFrame(col_dict)

print(book_store.head())
print(book_store.dtypes)

book_store['price'] = book_store['price'].apply(lambda x : float(x[2:]))

number_mapping = {'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
book_store['rating'] = book_store['rating'].apply(lambda x : number_mapping.get(x))

print(book_store.head())
print(book_store.dtypes)

book_store.to_csv('book_store.csv')
