import pandas as pd
import numpy as np

other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)
#print("The first 5 rows of the dataframe")
#print(df.tail(10))
#print(df.head(15))

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns = headers
#print(df.head(10))
df1=df.replace('?',np.NaN)
df=df1.dropna(subset=["price"], axis=0)
print(df.head(10))
#print(df1.head(10))
#print(df.columns)
df.to_csv("automobile.csv", index=False)
print(df.dtypes)
print(df.describe())
# describe all the columns in "df"
print(df.describe(include = "all"))
print(df[['length', 'compression-ratio']].describe())

print(df.info())