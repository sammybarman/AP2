from flask import Flask, render_template, request, render_template_string
import sqlite3, json, datetime

app = Flask(__name__)

conn = sqlite3.connect('hotels.db', check_same_thread = False)
cur = conn.cursor()

@app.route("/")
def renderPage():
    return render_template("index.html")

@app.route("/contact")
def contactPage():
    return render_template("contact.html")

@app.route("/checkout")
def checkoutPage():
    hotel_id = request.args.get('hotel_id')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    adults = request.args.get('adults')
    child = request.args.get('child')
    cur.execute('SELECT NAME, PRICE FROM HOTELS WHERE ID == ?', (hotel_id,))
    (name, price) = cur.fetchone()
    date_from_obj = datetime.datetime.strptime(date_from, '%b %d, %Y')
    date_to_obj = datetime.datetime.strptime(date_to, '%b %d, %Y')
    days = (date_to_obj - date_from_obj).days
    return render_template("checkout.html", data={'name': name, 'adults': adults, 'child': child, 'price': price, 'days': days})

@app.route("/gethoteldetails")
def hotelPage():
    hotel_id = request.args.get('hotel_id')
    location = request.args.get('location')
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    cur.execute('SELECT IMGS, NAME, INFO, GETTING_THERE, NEARBY_REST, NEARBY_ATTR, FEATURES, AMENITIES, FAQS FROM HOTELS WHERE ID == ?', (hotel_id,))
    hotel = cur.fetchone()
    img = json.loads(hotel[0])
    name = hotel[1]
    info = hotel[2]
    getting_there = json.loads(hotel[3])
    nearby_rest = json.loads(hotel[4])
    nearby_attr = json.loads(hotel[5])
    features = json.loads(hotel[6])
    amenities = json.loads(hotel[7])
    faqs = json.loads(hotel[8])
    cur.execute('SELECT COMMENT, RATING, USER, TITLE FROM COMMENTS WHERE HOTEL_ID == ?', (hotel_id,))
    rows = cur.fetchall()
    comments = []
    for row in rows:
        element = dict()
        element['body'] = row[0]
        element['rating'] = row[1]
        element['user'] = row[2]
        element['title'] = row[3]
        comments.append(element)
    return render_template("hotel.html", data={'hotel_id': hotel_id, 'location': location, 'date_from': date_from, 'date_to':date_to, 'img': img, 'name': name, 'info': info, 'getting_there': getting_there, 'nearby_rest': nearby_rest, 'near_attr': nearby_attr, 'features': features, 'amenities': amenities, 'faqs': faqs, 'comments': comments})

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
    cur.execute('SELECT IMGS, STARS, NAME, CITY, INFO, HOTELS.ID FROM CITIES, HOTELS WHERE CITIES.ID == CITY_ID AND CITY == ?', (location, ))
    hotels = []
    for row in cur.fetchall():
        element = dict()
        img_list = json.loads(row[0])
        if len(img_list) == 0:
            element['img'] = 'static/img/no_img.jpg'
        else:
            element['img'] = img_list[0]
        element['id'] = row[5]
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
    sql_query = 'SELECT IMGS, STARS, NAME, CITY, INFO, HOTELS.ID FROM CITIES, HOTELS{}'.format(wheres)
    # print(sql_query)
    cur.execute(sql_query, (js['city'],))
    hotels = []
    for row in cur.fetchall():
        element = dict()
        element['id'] = row[5]
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
            <button value="{{hotel['id']}}" onclick="getHotelDetails(this)" type="button" name="button" class="btn waves-effect cyan accent-3 black-text"style="margin-top: 10px">Show Prices</button>
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
