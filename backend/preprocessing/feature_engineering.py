import pandas as pd
import ast

# ==========================================
# Load merged dataset
# ==========================================

movies = pd.read_csv("backend/data/processed/movies_merged.csv")

# ==========================================
# Convert genres and keywords
# ==========================================

def convert(text):
    result = []

    for item in ast.literal_eval(text):
        result.append(item["name"])

    return result

# ==========================================
# Extract Top 3 Cast Members
# ==========================================

def convert_cast(text):
    result = []

    counter = 0

    for item in ast.literal_eval(text):

        if counter < 3:
            result.append(item["name"])
            counter += 1
        else:
            break

    return result

# ==========================================
# Extract Director
# ==========================================

def fetch_director(text):

    result = []

    for item in ast.literal_eval(text):

        if item["job"] == "Director":
            result.append(item["name"])
            break

    return result

# ==========================================
# Apply Functions
# ==========================================

movies["genres"] = movies["genres"].apply(convert)

movies["keywords"] = movies["keywords"].apply(convert)

movies["cast"] = movies["cast"].apply(convert_cast)

movies["crew"] = movies["crew"].apply(fetch_director)

# ==========================================
# Display Sample
# ==========================================

print("=" * 60)

print(movies[["title","genres","keywords","cast","crew"]].head())

print("=" * 60)

# ==========================================
# Save Dataset
# ==========================================

movies.to_csv(
    "backend/data/processed/movies_features.csv",
    index=False
)

print("\nFeature Engineering Completed Successfully!")