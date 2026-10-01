import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import ast

url = "movies_metadata.csv"
movies_df = pd.read_csv(url)

# print(movies_df.head())

movies_df.info()

# print(movies_df.describe())

def extract_genres(genres_str):
    try:
        genres = ast.literal_eval(genres_str)
        return [genre['name'] for genre in genres]
    except(ValueError, TypeError):
        return []

movies_df['genres'] = movies_df['genres'].apply(extract_genres)
print(movies_df['genres'])


movies_df['budget'] = pd.to_numeric(movies_df['budget'], errors='coerce')
movies_df['revenue'] = pd.to_numeric(movies_df['revenue'], errors='coerce')

movies_df['release_year'] = pd.to_datetime(movies_df['release_date'], errors='coerce').dt.year
# print(movies_df[['release_date', 'original_language']])
movies_df['popularity'] = pd.to_numeric(movies_df['popularity'], errors='coerce')

movies_df.dropna(subset=['budget', 'revenue', 'popularity', 'release_year'], inplace=True)

genre_exploded = movies_df[['title', 'release_year', 'budget', 'revenue', 'genres']].explode('genres')
print(genre_exploded)

genre_count = genre_exploded['genres'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=genre_count.index, y=genre_count.values)
plt.title("Кількість фільмів за жанрами")
plt.xlabel("Жанр")
plt.ylabel("Кількість")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

average_popularity = movies_df.groupby('release_year')['popularity'].mean()
plt.figure(figsize=(12, 6))
plt.plot(average_popularity.index, average_popularity.values)
plt.title("Середня популярність фільмів за роками")
plt.xlabel("Рік")
plt.ylabel("Середня популярність")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(movies_df['budget'],movies_df['revenue'], alpha=0.5)
plt.title("Залежність між бюджетом і прибутком")
plt.xlabel("Бюджет")
plt.ylabel("Прибуток")
plt.grid(True)
plt.tight_layout()
plt.show()


