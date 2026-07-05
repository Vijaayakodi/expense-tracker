from flask import Flask, render_template
from flask_cors import CORS
from routes import transaction_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(transaction_bp)

@app.route("/")
def home():
    return render_template("index.html")

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )