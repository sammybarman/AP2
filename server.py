from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def renderPage():
    return render_template("index.html")

@app.route("/product")
def product_page():
    return render_template("product.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/why")
def why_page():
    return render_template("why.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
