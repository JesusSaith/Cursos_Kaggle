# Your code here
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))

reindexed = reviews.rename_axis('wines', axis='rows')

gaming_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("../input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"
combined_products = pd.concat([gaming_products, movie_products])

powerlifting_combined = powerlifting_meets.set_index("MeetID").join(powerlifting_competitors.set_index("MeetID"))