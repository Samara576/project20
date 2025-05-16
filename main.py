from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Салам, бул Flask колдонмо!"

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    result = data["a"] + data["b"]
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)