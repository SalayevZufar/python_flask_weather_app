from flask import Flask, render_template,request
import requests, json,urllib

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home(): 
    if request.method == 'POST':
        city = request.form['city_name']
        
        data = {}
        data['q'] = city
        data['appid'] = '2f5570b8224e6dda99514fa247a7caac'
        data['units'] = 'metric'

        url_values = urllib.parse.urlencode(data)
        url = 'http://api.openweathermap.org/data/2.5/forecast'
        full_url = url + '?' + url_values
        response = requests.get(full_url)
        if response.status_code == 200:

            data = urllib.request.urlopen(full_url)
            info = json.loads(data.read().decode('utf8'))
            city_name = info['city']['name']
            country_name = info['city']['country']
            return render_template("home.html",city=city_name,country=country_name , data=info)
        else:
           return render_template("home.html",data="Eror city name") 
    else:
        return render_template("home.html",data="")

    
    
if __name__ == "__main__":
    app.run(debug=True)