from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask App Deployed Successfully!"

@app.route("/api")
def api():
    return jsonify({
        "message": "API is working!",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)