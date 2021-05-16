from flask import Flask, render_template, url_for, request, redirect
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Present_Price = Present_Price/6.1
        Present_Price = Present_Price-1.14
        car_popularity_rare_cars = request.form['popularity']
        if (car_popularity_rare_cars == 'popular'):
            car_popularity_rare_cars = 0
        else:
            car_popularity_rare_cars = 1

        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        if(Fuel_Type_Petrol=='Petrol'):
            Fuel_Type_Petrol=1
        else:
            Fuel_Type_Petrol=0
        Year=2021-Year
        Year = Year/2.89
        Year = Year - 2.55
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.form['Transmission_Mannual']
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Year,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual,car_popularity_rare_cars]])
        output=round(prediction[0],0)
        if output<0:
            return render_template('predit.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('predit.html',prediction_text="You Can Sell The Car at {} Lks".format(output))
    else:
        return render_template('predit.html')

if __name__=="__main__":
    app.run(debug=True)
