from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderPage():
    return render_template("index.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
