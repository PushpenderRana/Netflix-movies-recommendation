import pandas as pd
from nltk.stem.porter import PorterStemmer

# ==========================================
# Load feature engineered dataset
# ==========================================

movies = pd.read_csv("backend/data/processed/movies_features.csv")

# ==========================================
# Convert overview into list
# ==========================================

# Save original overview for UI
movies["overview_text"] = movies["overview"]

# Process overview for recommendation tags
movies["overview"] = movies["overview"].apply(lambda x: x.split())
# ==========================================
# Remove spaces from names
# ==========================================

movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ", "") for i in eval(x)]
)

movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ", "") for i in eval(x)]
)

movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ", "") for i in eval(x)]
)

movies["crew"] = movies["crew"].apply(
    lambda x: [i.replace(" ", "") for i in eval(x)]
)

# ==========================================
# Create Tags
# ==========================================

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

# ==========================================
# Keep useful columns only
# ==========================================
new_df = movies[
    [
        "id",
        "title",
        "overview_text",
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
        "tags"
    ]
].copy()

new_df.rename(
    columns={"overview_text": "overview"},
    inplace=True
)
# ==========================================
# Convert list to string
# ==========================================

new_df["tags"] = new_df["tags"].apply(
    lambda x: " ".join(x)
)
# ==========================================
# Convert to lowercase
# ==========================================

new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())

# ==========================================
# Stemming
# ==========================================

ps = PorterStemmer()

def stem(text):
    words = []

    for word in text.split():
        words.append(ps.stem(word))

    return " ".join(words)

new_df["tags"] = new_df["tags"].apply(stem)

# ==========================================
# Preview
# ==========================================

print(new_df.head())

# ==========================================
# Save final dataset
# ==========================================

new_df.to_csv(
    "backend/data/processed/final_movies.csv",
    index=False
)

print("\nFinal dataset saved successfully!")