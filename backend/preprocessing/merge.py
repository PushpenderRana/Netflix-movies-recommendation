import pandas as pd

# ==========================================
# Load Cleaned Datasets
# ==========================================

movies = pd.read_csv("backend/data/processed/movies_clean.csv")
credits = pd.read_csv("backend/data/processed/credits_clean.csv")

print("=" * 60)
print("Movies Shape :", movies.shape)
print("Credits Shape:", credits.shape)
print("=" * 60)

# ==========================================
# Rename movie_id to id
# ==========================================

credits.rename(columns={"movie_id": "id"}, inplace=True)

# ==========================================
# Remove duplicate title column from credits
# ==========================================

if "title" in credits.columns:
    credits.drop(columns=["title"], inplace=True)

# ==========================================
# Merge Movies and Credits
# ==========================================

movies = movies.merge(credits, on="id")

print("\nMerged Shape:", movies.shape)

# ==========================================
# Display columns after merging
# ==========================================

print("\nColumns after merge:\n")
print(movies.columns.tolist())



movies = movies[
    [
        "id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
        "vote_average",
        "vote_count",
        "popularity",
        "release_date",
        "runtime",
        "tagline",
    ]
]

print("\nFinal Shape:", movies.shape)


print("\nMissing Values:\n")
print(movies.isnull().sum())



movies.dropna(inplace=True)

print("\nShape After Removing Missing Values:")
print(movies.shape)



movies.drop_duplicates(inplace=True)

print("\nShape After Removing Duplicate Rows:")
print(movies.shape)



print("\nFirst 5 Rows:\n")
print(movies.head())



movies.to_csv(
    "backend/data/processed/movies_merged.csv",
    index=False
)

print("\n" + "=" * 60)
print("Merged dataset saved successfully!")
print("Location: backend/data/processed/movies_merged.csv")
print("=" * 60)