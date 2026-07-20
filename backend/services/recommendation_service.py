import pickle

movies = pickle.load(
    open("models/movies.pkl", "rb")
)

similarity = pickle.load(
    open("models/similarity.pkl", "rb")
)


# ---------------------------------------
# Recommendation
# ---------------------------------------

def recommend_movies(movie):

    movie = movie.lower()

    matched = movies[
        movies["title"].str.lower() == movie
    ]

    if matched.empty:
        return {
            "success": False,
            "message": "Movie not found."
        }

    searched_movie = matched.iloc[0]

    index = searched_movie.name

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for item in movie_list:

        recommended_movie = movies.iloc[item[0]]

        recommendations.append({
            "id": int(recommended_movie["id"]),
            "title": recommended_movie["title"],
            "overview": recommended_movie["overview"],
            "genres": recommended_movie["genres"],
            "vote_average": float(recommended_movie["vote_average"]),
            "vote_count": int(recommended_movie["vote_count"]),
            "release_date": recommended_movie["release_date"],
            "runtime": int(recommended_movie["runtime"]),
            "tagline": "" if str(recommended_movie["tagline"]) == "nan" else recommended_movie["tagline"],
            "popularity": float(recommended_movie["popularity"])
        })

    return {
        "success": True,

        "searched_movie": {
            "id": int(searched_movie["id"]),
            "title": searched_movie["title"],
            "overview": searched_movie["overview"],
            "genres": searched_movie["genres"],
            "vote_average": float(searched_movie["vote_average"]),
            "vote_count": int(searched_movie["vote_count"]),
            "release_date": searched_movie["release_date"],
            "runtime": int(searched_movie["runtime"]),
            "tagline": "" if str(searched_movie["tagline"]) == "nan" else searched_movie["tagline"],
            "popularity": float(searched_movie["popularity"])
        },

        "recommendations": recommendations
    }


# ---------------------------------------
# Get All Movies
# ---------------------------------------

def get_all_movies():

    return movies["title"].tolist()


# ---------------------------------------
# Search Movie
# ---------------------------------------

def search_movies(name):

    name = name.lower()

    result = movies[
        movies["title"]
        .str.lower()
        .str.contains(name, na=False)
    ]

    return result["title"].tolist()[:10]