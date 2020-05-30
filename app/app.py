from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "This is the Dad-A-Base api."


@app.route("/random")
def random():
    data = {"joke": "Random joke"}
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=os.environ.get("PORT", 80))
