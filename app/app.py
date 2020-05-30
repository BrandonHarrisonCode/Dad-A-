from flask import Flask, jsonify
from flask_cors import CORS

from Database import Database

app = Flask(__name__)
CORS(app)

database = Database()


@app.route("/")
def index():
    return "This is the Dad-A-Base api."


@app.route("/random")
def random():
    id, joke = database.get_random_joke()
    data = {"id": id, "joke": joke}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=os.environ.get("PORT", 80))
