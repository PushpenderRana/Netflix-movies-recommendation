from flask import Blueprint, request, jsonify
from services.recommendation_service import recommend_movies
from llm import explain_recommendations
import traceback
from services.recommendation_service import (
    recommend_movies,
    get_all_movies,
    search_movies
)

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)


@recommendation_bp.route("/recommend/<movie>", methods=["GET"])
def recommend_with_llm(movie):

    result = recommend_movies(movie)

    if not result["success"]:
        return jsonify(result)

    explanations = explain_recommendations(
        result["searched_movie"],
        result["recommendations"]
    )

    result["llm_explanation"] = explanations

    return jsonify(result)



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

        # Recommendation
        result = recommend_movies(movie)

        print("\n========== Recommendation ==========")
        print(result)

        if result["success"]:

            print("\n========== Calling LLM ==========")

            explanations = explain_recommendations(
                result["searched_movie"],
                result["recommendations"]
            )

            print("\n========== LLM Output ==========")
            print(explanations)

            result["llm_explanation"] = explanations

        print("\n========== Final Response ==========")
        print(result)

        return jsonify(result)

    except Exception as e:

        traceback.print_exc()

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
    


