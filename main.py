from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = []

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route('/submit', methods=["POST"])
def submit():
    items.append(request.form["item"])
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0")