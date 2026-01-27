from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello CI/CD Security Pipeline!"

@app.route("/greet")
def greet():
    name = escape(request.args.get("name", "Guest"))
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
