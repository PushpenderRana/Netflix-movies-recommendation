from flask import Blueprint, request, jsonify

from services.recommendation_service import (
    recommend_movies,
    get_all_movies,
    search_movies
)

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)



# ---------------------------------------
# Get Recommendation
# ---------------------------------------

@recommendation_bp.route("/recommend", methods=["POST"])
def recommend():

    try:

        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "Request body must be JSON."
            }), 400

        movie = data.get("movie")

        if not movie:
            return jsonify({
                "error": "Movie name is required."
            }), 400

        result = recommend_movies(movie)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ---------------------------------------
# Get All Movies
# ---------------------------------------

@recommendation_bp.route("/movies", methods=["GET"])
def movies():

    try:

        result = get_all_movies()

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ---------------------------------------
# Search Movies
# ---------------------------------------

@recommendation_bp.route("/search", methods=["GET"])
def search():

    try:

        movie = request.args.get("movie")

        if not movie:
            return jsonify([])

        result = search_movies(movie)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500