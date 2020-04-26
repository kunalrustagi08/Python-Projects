import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(10))

view_count_by_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(view_count_by_source)

ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(lambda x : 'True' if x == x  else 'False')
print(ad_clicks.head(10))

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
columns = 'is_click',
index = 'utm_source',
values = 'user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot['True'] * 100/ (clicks_pivot['True']+clicks_pivot['False'])
print(clicks_pivot)

A_count = ad_clicks[ad_clicks['experimental_group'] == 'A'].user_id.count()
B_count = ad_clicks[ad_clicks['experimental_group'] == 'B'].user_id.count()
print(A_count, B_count)
'''
AB_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
'''

greater_count = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(greater_count)

a_clicks = ad_clicks[ad_clicks['experimental_group']=='A']
b_clicks = ad_clicks[ad_clicks['experimental_group']=='B']
print(a_clicks.head())
print(b_clicks.head())

day_a_clicks = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
day_a_pivot = day_a_clicks.pivot(columns='is_click', index= 'day', values='user_id').reset_index()
day_a_pivot['percent'] = day_a_pivot['True'] *100 / (day_a_pivot['True'] + day_a_pivot['False'])
print(day_a_pivot)

day_b_clicks = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
day_b_pivot = day_b_clicks.pivot(columns='is_click', index= 'day', values='user_id').reset_index()
day_b_pivot['percent'] = day_b_pivot['True'] *100 / (day_b_pivot['True'] + day_b_pivot['False'])
print(day_b_pivot)
