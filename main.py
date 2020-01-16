from flask import Flask, render_template, request, redirect
from datetime import datetime
import operator

app = Flask(__name__)

highscores = []


@app.route("/")
def index():
    return render_template("index.html", highscores=sorted(highscores, key=lambda i: i['score'], reverse=True))

@app.route('/submit', methods=["POST"])
def submit():
    highscores.append({
        "score": int(request.form["score"]),
        "name": request.form["name"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return "success", 201

if __name__ == "__main__":
    app.run(host="0.0.0.0")