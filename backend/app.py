from flask import Flask
import os
from routes.recommendation import recommendation_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(recommendation_bp)


@app.route("/", methods=["GET"])
def home():
    return {
        "status": "success",
        "message": "Netflix Recommendation API is Running"
    }




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )