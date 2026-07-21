import pandas as pd
from nltk.stem.porter import PorterStemmer


movies = pd.read_csv("backend/data/processed/movies_features.csv")


movies["overview_text"] = movies["overview"]

# Process overview for recommendation tags
movies["overview"] = movies["overview"].apply(lambda x: x.split())
# Remove spaces from names

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

# Create Tags

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)


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


new_df["tags"] = new_df["tags"].apply(
    lambda x: " ".join(x)
)


new_df["tags"] = new_df["tags"].apply(lambda x: x.lower())



ps = PorterStemmer()

def stem(text):
    words = []

    for word in text.split():
        words.append(ps.stem(word))

    return " ".join(words)

new_df["tags"] = new_df["tags"].apply(stem)



print(new_df.head())



new_df.to_csv(
    "backend/data/processed/final_movies.csv",
    index=False
)

print("\nFinal dataset saved successfully!")