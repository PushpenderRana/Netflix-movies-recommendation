import os
import pandas as pd



os.makedirs("backend/data/processed", exist_ok=True)

# Load datasets

movies = pd.read_csv("backend/data/raw/tmdb_5000_movies.csv")
credits = pd.read_csv("backend/data/raw/tmdb_5000_credits.csv")

# Display basic information

print("=" * 60)
print("MOVIES DATASET")
print("=" * 60)

print("\nShape:")
print(movies.shape)

print("\nColumns:")
print(movies.columns.tolist())

print("\nData Types:")
print(movies.dtypes)

print("\nMissing Values:")
print(movies.isnull().sum())

print("\nDuplicate Rows:")
print(movies.duplicated().sum())


print("\n" + "=" * 60)
print("CREDITS DATASET")
print("=" * 60)

print("\nShape:")
print(credits.shape)

print("\nColumns:")
print(credits.columns.tolist())

print("\nData Types:")
print(credits.dtypes)

print("\nMissing Values:")
print(credits.isnull().sum())

print("\nDuplicate Rows:")
print(credits.duplicated().sum())

# Remove duplicate rows

movies.drop_duplicates(inplace=True)
credits.drop_duplicates(inplace=True)

print("\nDuplicate rows removed.")

# Check duplicate movie IDs

print("\nUnique Movie IDs")

print("Movies :", movies["id"].nunique())
print("Credits:", credits["movie_id"].nunique())



movies.to_csv(
    "backend/data/processed/movies_clean.csv",
    index=False
)

credits.to_csv(
    "backend/data/processed/credits_clean.csv",
    index=False
)

print("\nCleaned datasets saved successfully!")