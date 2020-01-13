from flask import Flask, render_template, request, redirect

app = Flask(__name__)

highscores = []

stats = {
    "highscores":highscore 
    "names":name
    "dates":date
        }

@app.route("/")
def index():
    return render_template("index.html", highscores=highscores)

@app.route('/submit', methods=["POST"])
def submit():
    highscores.append(request.form["highscore"])
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0")