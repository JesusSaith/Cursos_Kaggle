# Your code here
desc = reviews.description

first_description = reviews.description.iloc[0]

first_row = first_row = reviews.iloc[0]

first_descriptions = reviews.description.iloc[:10]

sample_reviews = reviews.loc[[1, 2, 3, 5, 8]]

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]
print(df)

cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]
print(df)

italian_wines = reviews[reviews.country == 'Italy']

top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
