from flask import Flask, render_template, request, render_template_string
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

@app.route("/getfilterhotels", methods=['POST'])
def getfilterhotels():
    js= request.get_json()
    wheres = ' WHERE CITIES.ID == CITY_ID AND CITY == ?'
    for i in js['amenities']:
        wheres += ' AND AMENITIES LIKE "%{}%"'.format(i)
    for i in js['features']:
        wheres += ' AND FEATURES LIKE "%{}%"'.format(i)
    if len(js['rating']) > 0:
        wheres += ' AND (STARS == {}'.format(js['rating'][0])
        for i in js['rating'][1:]:
            wheres += ' OR STARS == {}'.format(i)
        wheres += ')'
    wheres += ' AND PRICE >= {} AND PRICE <= {}'.format(js['price_min'], js['price_max'])
    sql_query = 'SELECT IMGS, STARS, NAME, CITY, INFO FROM CITIES, HOTELS{}'.format(wheres)
    # print(sql_query)
    cur.execute(sql_query, (js['city'],))
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
    html_string = '''
    {% for hotel in data['hotels'] %}
      <div class="indhotel" style="border:2px solid indigo; margin:10px">
        <div class="row">
          <div class="col s3 m3 l3 center" style="margin-top:5%">
            <img src="{{hotel['img']}}" alt="">
            <div class="cyan accent-3" style="width:70px; height:30px; margin-left:35%; margin-top:20px">
              <p style="color: black" class="valign-center">{{hotel['stars']}} stars</p>
            </div>
            <button type="button" name="button" class="btn waves-effect cyan accent-3 black-text"style="margin-top: 10px">Show Prices</button>
          </div>
          <div class="col s7 m7 l7">
            <p style="font-size: 20px" class="black-text"><b>{{hotel['name']}}</b></p>
            <span class="black-text">{{hotel['city']}}, India</span>
            <p>{{hotel['info']}}</p>
          </div>
        </div>
      </div>
    {% endfor %}
    '''
    return render_template_string(html_string, data={'hotels': hotels})




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
