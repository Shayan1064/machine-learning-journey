
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/handle-login", methods=["GET", "POST"])
def handle_login():
    if request.method == "POST":
        print(request.form)

        name = request.form["username"]
        password = request.form["password"]

        return f"<p>Welcome {name}!</p>"

    return "<p>This route is to handle login</p>"

@app.route("/student", methods=["GET"])
def student():

    data = {
        "name": "Shayan",
        "field": "Artificial Intelligence",
        "skill": "Python"
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
