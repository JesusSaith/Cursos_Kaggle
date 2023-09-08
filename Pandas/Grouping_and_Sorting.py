reviews_written = reviews.groupby('taster_twitter_handle').size()

best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()

price_extremes = reviews.groupby('variety').price.agg([min, max])

sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)

reviews.groupby('taster_name').points.mean()

reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)