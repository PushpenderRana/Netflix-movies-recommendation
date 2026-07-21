import pandas as pd
import ast



movies = pd.read_csv("backend/data/processed/movies_merged.csv")



def convert(text):
    result = []

    for item in ast.literal_eval(text):
        result.append(item["name"])

    return result


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



def fetch_director(text):

    result = []

    for item in ast.literal_eval(text):

        if item["job"] == "Director":
            result.append(item["name"])
            break

    return result



movies["genres"] = movies["genres"].apply(convert)

movies["keywords"] = movies["keywords"].apply(convert)

movies["cast"] = movies["cast"].apply(convert_cast)

movies["crew"] = movies["crew"].apply(fetch_director)



print("=" * 60)

print(movies[["title","genres","keywords","cast","crew"]].head())

print("=" * 60)


movies.to_csv(
    "backend/data/processed/movies_features.csv",
    index=False
)

print("\nFeature Engineering Completed Successfully!")