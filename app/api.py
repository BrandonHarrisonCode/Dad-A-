from flask import Flask, jsonify
from flask_cors import CORS

from .database import Database

api = Flask(__name__)
CORS(api)

database = Database()


@api.route("/")
def index():
    return "This is the Dad-A-Base api."


@api.route("/random")
def random():
    id, joke = database.get_random_joke()
    data = {"id": id, "joke": joke}
    return jsonify(data)


if __name__ == "__main__":
    api.run(host="0.0.0.0", debug=False, port=os.environ.get("PORT", 80))
