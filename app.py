from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Hello, world!")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/echo")
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify(data=data)


if __name__ == "__main__":
    app.run(debug=True)