from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    drink = request.form["drink"]
    nickname = request.form["nickname"]

    return f"Drink: {drink}, Nickname: {nickname}"

if __name__ == "__main__":
    app.run(debug=True, port=5001)