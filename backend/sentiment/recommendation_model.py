import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ==========================================
# Load Dataset
# ==========================================

movies = pd.read_csv("backend/data/processed/final_movies.csv")

print("Dataset Shape:", movies.shape)

# ==========================================
# Convert Tags into Vectors
# ==========================================

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(movies["tags"]).toarray()

print("Vector Shape:", vectors.shape)

# ==========================================
# Calculate Cosine Similarity
# ==========================================

similarity = cosine_similarity(vectors)

print("Similarity Shape:", similarity.shape)

# ==========================================
# Recommendation Function
# ==========================================

def recommend(movie):

    movie = movie.lower()

    matched = movies[
        movies["title"].str.lower() == movie
    ]

    if matched.empty:
        print("Movie not found.")
        return

    movie_index = matched.index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    print("\nRecommended Movies:\n")

    for i in movie_list:
        print(movies.iloc[i[0]].title)

# ==========================================
# Test
# ==========================================

recommend("Avatar")

# ==========================================
# Save Models
# ==========================================

pickle.dump(
    movies,
    open("backend/models/movies.pkl", "wb")
)

pickle.dump(
    similarity,
    open("backend/models/similarity.pkl", "wb")
)

print("\nModels saved successfully!")