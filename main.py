import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns

url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

print(movies_df.head())

movies_df.info()

print(movies_df.describe())

def extract_genres(genres_str):
    try:
        genres = ast
