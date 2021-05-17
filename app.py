# -*- coding: utf-8 -*-
"""
Created on Sun May 16 17:48:25 2021

@author: harsh
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
app = Flask(__name__)
model = pickle.load(open('insurance_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        
        Intercept = 1.0
        Insured=float(request.form['Insured_amt'])
        Kilometres=int(request.form['Kilmeters_category'])
        
        if(Kilometres==2):
            Kilometres_2 = 1
            Kilometres_3 = 0
            Kilometres_4 = 0
            Kilometres_5 = 0
        elif(Kilometres==3):
            Kilometres_2 = 0
            Kilometres_3 = 1
            Kilometres_4 = 0
            Kilometres_5 = 0
        elif(Kilometres==4):
            Kilometres_2 = 0
            Kilometres_3 = 0
            Kilometres_4 = 1
            Kilometres_5 = 0
        else:
            Kilometres_2 = 0
            Kilometres_3 = 0
            Kilometres_4 = 0
            Kilometres_5 = 1
        Zone=int(request.form['Zone'])
        
        if(Zone==2):
            Zone_2 = 1
            Zone_3 = 0
            Zone_4 = 0
            Zone_5 = 0
            Zone_6 = 0
            Zone_7 = 0
        elif(Zone==3):
            Zone_2 = 0
            Zone_3 = 1
            Zone_4 = 0
            Zone_5 = 0
            Zone_6 = 0
            Zone_7 = 0
        elif(Zone==4):
            Zone_2 = 0
            Zone_3 = 0
            Zone_4 = 1
            Zone_5 = 0
            Zone_6 = 0
            Zone_7 = 0
        elif(Zone==5):
            Zone_2 = 0
            Zone_3 = 0
            Zone_4 = 0
            Zone_5 = 1
            Zone_6 = 0
            Zone_7 = 0
        elif(Zone==6):
            Zone_2 = 0
            Zone_3 = 0
            Zone_4 = 0
            Zone_5 = 0
            Zone_6 = 1
            Zone_7 = 0
        else:
            Zone_2 = 0
            Zone_3 = 0
            Zone_4 = 0
            Zone_5 = 0
            Zone_6 = 0
            Zone_7 = 1
        Bonus=int(request.form['Bonus'])
        if(Bonus==2):
            Bonus_2 = 1
            Bonus_3 = 0
            Bonus_4 = 0
            Bonus_5 = 0
            Bonus_6 = 0
            Bonus_7 = 0
        elif(Bonus==3):
            Bonus_2 = 0
            Bonus_3 = 1
            Bonus_4 = 0
            Bonus_5 = 0
            Bonus_6 = 0
            Bonus_7 = 0
        elif(Bonus==4):
            Bonus_2 = 0
            Bonus_3 = 0
            Bonus_4 = 1
            Bonus_5 = 0
            Bonus_6 = 0
            Bonus_7 = 0
        elif(Bonus==5):
            Bonus_2 = 0
            Bonus_3 = 0
            Bonus_4 = 0
            Bonus_5 = 1
            Bonus_6 = 0
            Bonus_7 = 0
        elif(Bonus==6):
            Bonus_2 = 0
            Bonus_3 = 0
            Bonus_4 = 0
            Bonus_5 = 0
            Bonus_6 = 1
            Bonus_7 = 0
        else:
            Bonus_2 = 0
            Bonus_3 = 0
            Bonus_4 = 0
            Bonus_5 = 0
            Bonus_6 = 0
            Bonus_7 = 1
        
        Make=int(request.form['Make'])
        if(Make==2):
            Make_2 = 1
            Make_3 = 0
            Make_4 = 0
            Make_5 = 0
            Make_6 = 0
            Make_7 = 0
            Make_8 = 0
            Make_9 = 0
        elif(Make==3):
            Make_2 = 0
            Make_3 = 1
            Make_4 = 0
            Make_5 = 0
            Make_6 = 0
            Make_7 = 0
            Make_8 = 0
            Make_9 = 0
        elif(Make==4):
            Make_2 = 0
            Make_3 = 0
            Make_4 = 1
            Make_5 = 0
            Make_6 = 0
            Make_7 = 0
            Make_8 = 0
            Make_9 = 0
        elif(Make==5):
            Make_2 = 0
            Make_3 = 0
            Make_4 = 0
            Make_5 = 1
            Make_6 = 0
            Make_7 = 0
            Make_8 = 0
            Make_9 = 0
        elif(Make==6):
            Make_2 = 0
            Make_3 = 0
            Make_4 = 0
            Make_5 = 0
            Make_6 = 1
            Make_7 = 0
            Make_8 = 0
            Make_9 = 0
        elif(Make==7):
            Make_2 = 0
            Make_3 = 0
            Make_4 = 0
            Make_5 = 0
            Make_6 = 0
            Make_7 = 1
            Make_8 = 0
            Make_9 = 0
        elif(Make==8):
            Make_2 = 0
            Make_3 = 0
            Make_4 = 0
            Make_5 = 0
            Make_6 = 0
            Make_7 = 0
            Make_8 = 1
            Make_9 = 0
        else:
            Make_2 = 0
            Make_3 = 0
            Make_4 = 0
            Make_5 = 0
            Make_6 = 0
            Make_7 = 0
            Make_8 = 0
            Make_9 = 1
        
        
        prediction=model.predict([[Intercept, Kilometres_2,Kilometres_3,Kilometres_4,Kilometres_5,
                                   Zone_2,Zone_3,Zone_4,Zone_5,Zone_6,Zone_7,
                                   Bonus_2,Bonus_3,Bonus_4,Bonus_5,Bonus_6,Bonus_7,
                                   Make_2,Make_3,Make_4,Make_5,Make_6,Make_7,Make_8,Make_9,
                                   Insured]])
        
        output=round(prediction[0],0)

    
        return render_template('index.html',prediction_text="The Predicted Payment Amount is {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)