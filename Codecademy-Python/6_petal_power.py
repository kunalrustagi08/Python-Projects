import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory.iloc[0:10,:]
print(staten_island)

product_request = staten_island['product_description']
print(product_request)

seed_request = inventory[(inventory['location'] == 'Brooklyn') & (inventory['product_type'] == 'seeds')]
print(seed_request)

inventory['in_stock'] = inventory.quantity.apply(lambda x : 'True' if x > 0 else 'False')
print(inventory)

inventory['total_value'] = inventory['price'] * inventory['quantity']
print(inventory)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)
