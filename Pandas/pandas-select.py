import pandas as pd

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
pd.set_option('display.max_rows', 5)
print(reviews)

print('\n select country from winemag\n')
print(reviews.country)

print('\n sub-dataset\n select country from winemag\n')
review_country = reviews['country']
print(review_country)
