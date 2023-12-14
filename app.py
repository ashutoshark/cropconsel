from flask import Flask,request,render_template
import numpy as np
import pandas
import sklearn
import pickle
import requests
# importing model
model = pickle.load(open('models/model2.pkl','rb'))
sc = pickle.load(open('models/standscaler2.pkl','rb'))
# ms = pickle.load(open('minmaxscaler.pkl','rb'))

# creating flask app
app = Flask(__name__)

API_KEY = "14eb4cb99a4139d1aca0b7e98b640e26"
@app.route('/', methods = ['GET', 'POST'])
# this is weather api implemntaion
def weather():
    city = 'New York'  # Default city
    weather_data = None

    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather_data(city)

    return render_template('index.html', city=city, weather_data=weather_data)

def get_weather_data(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # You can change this to 'imperial' or 'standard' if needed
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temperature': data['main']['temp'],
            'humidity':data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather_info
    else:
        return None



@app.route("/predict",methods=['POST'])
def predict():
    # nitro=int(request.form['Nitrogen'])
    # N=0
    # if(nitro>0 and nitro<140):
    #     N=nitro
    N = request.form['Nitrogen']
    # phos=int(request.form['Phosporus'])
    # P=0
    # if(phos>=5 or phos<=145):
    #     P=phos
    P = request.form['Phosporus']
    # potas=int(request.form['Potassium'])
    # K=0
    # if(potas>=5 or potas<=205):
    #     K=potas
    K = request.form['Potassium']
    # tempr=int(request.form['Temperature'])
    # temp=0
    # if(tempr>=8 or tempr<=44):
    #     temp=tempr
    temp = request.form['Temperature']
    # humi=int(request.form['Humidity'])
    # humidity=0
    # if(humi>=14 or humi<=100):
    #     humidity=humi
    humidity = request.form['Humidity']
    # phi=int(request.form['Ph'])
    # ph=0
    # if(phi>=3 or phi<=10 ):
    #     ph=phi
    ph = request.form['Ph']
    # rain=int(request.form['Rainfall'])
    # rainfall=0
    # if(rain>=20 or rain<=300):
    #     rainfall=rain
    rainfall = request.form['Rainfall']
    
    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    # scaled_features = ms.transform(single_pred)
    final_features = sc.transform(single_pred)
    prediction = model.predict(final_features)

   


    crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
    crop_img=0+prediction[0]
    return render_template('index.html',result = result,crop_img=crop_img)




# python main
if __name__ == "__main__":
    app.run(debug=True)