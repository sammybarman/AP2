from flask import Flask, render_template, request
import sqlite3, json

app = Flask(__name__)

conn = sqlite3.connect('hotels.db', check_same_thread = False)
cur = conn.cursor()

@app.route("/")
def renderPage():
    return render_template("index.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/gethotels")
def infoPage():
    location = request.args.get('location')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    cur.execute('SELECT AMENITIES, FEATURES FROM HOTELS')
    amenities = []
    features = []
    for row in cur.fetchall():
        amenities.extend(json.loads(row[0]))
        features.extend(json.loads(row[1]))
    amenities = list(set(amenities))
    features = list(set(features))
    cur.execute('SELECT IMGS, STARS, NAME, CITY, INFO FROM CITIES, HOTELS WHERE CITIES.ID == CITY_ID AND CITY == ?', (location, ))
    hotels = []
    for row in cur.fetchall():
        element = dict()
        img_list = json.loads(row[0])
        if len(img_list) == 0:
            element['img'] = 'static/img/no_img.jpg'
        else:
            element['img'] = img_list[0]
        element['stars'] = row[1]
        element['name'] = row[2]
        element['city'] = row[3]
        element['info'] = row[4]
        hotels.append(element)
    return render_template("info.html", data={'hotels': hotels, 'features': features, 'amenities': amenities, 'date_from': date_from, 'date_to': date_to, 'location': location})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
