import pandas as pd
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print("\n sub-dataset \n select top 1 * from winesmag \n")
reviews_iloc_n = reviews.iloc[100]
print (reviews_iloc_n)

print("\n sub-dataset \n select country from winesmag \n")
reviews_country = reviews.iloc[:,0]
print(reviews_country)

print("\n sub-dataset \n select top 3 country from winesmag \n")
reviews_country_top3 = reviews.iloc[:,3]
print(reviews_country_top3)

print("\n sub-dataset \n select country from winesmag \n")
reviews_country_r2_r3 = reviews.iloc[1:3,0]
print(reviews_country_r2_r3)

print("\n sub-dataset \n select country from winesmag \n")
reviews_country_r1_r2_r3 = reviews.iloc[[0, 1, 2], 0]
print(reviews_country_r1_r2_r3)

print("\n sub-dataset \n select country from winesmag \n")
reviews_country_descrip_r1_r2_r3 = reviews.iloc[[0,1,2],[0,1]]
print(reviews_country_descrip_r1_r2_r3)



