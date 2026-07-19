import requests
from config import API_URL


def get_movies():
    """Fetch all movie names."""

    try:
        response = requests.get(f"{API_URL}/movies")
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException:
        return []


def recommend_movie(movie):
    """Get movie recommendations."""

    try:
        response = requests.post(
            f"{API_URL}/recommend",
            json={"movie": movie}
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        return {
            "success": False,
            "message": str(e)
        }