from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/codechef")
def codechef():
    return render_template("codechef.html")

@app.route("/leetcode")
def leetcode():
    return render_template("leetcode.html")

@app.route("/sololearn")
def sololearn():
    return render_template("sololearn.html")


if __name__ == '__main__':
    app.run(debug=True)