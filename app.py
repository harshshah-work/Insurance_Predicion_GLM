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
        Kilometres_2 = 0
        Kilometres_3 = 0
        Kilometres_4 = 0
        Kilometres_5 = 0
        Zone_2 = 0
        Zone_3 = 0
        Zone_4 = 0
        Zone_5 = 0
        Zone_6 = 0
        Zone_7 = 0
        Bonus_2 = 0
        Bonus_3 = 0
        Bonus_4 = 0
        Bonus_5 = 0
        Bonus_6 = 0
        Bonus_7 = 0
        Make_2 = 0
        Make_3 = 0
        Make_4 = 0
        Make_5 = 0
        Make_6 = 0
        Make_7 = 0
        Make_8 = 0
        Make_9 = 0
        
        if(Kilometres==2):
            Kilometres_2 = 1
          
        elif(Kilometres==3):
    
            Kilometres_3 = 1
            
        elif(Kilometres==4):
            Kilometres_4 = 1
           
        else:
      
            Kilometres_5 = 1
        Zone=int(request.form['Zone'])
        
        if(Zone==2):
            Zone_2 = 1
            
        elif(Zone==3):
            
            Zone_3 = 1
           
        elif(Zone==4):
        
            Zone_4 = 1
            
        elif(Zone==5):
         
            Zone_5 = 1
           
        elif(Zone==6):
        
            Zone_6 = 1
           
        else:
         
            Zone_7 = 1
        Bonus=int(request.form['Bonus'])
        if(Bonus==2):
            Bonus_2 = 1
            
        elif(Bonus==3):
            
            Bonus_3 = 1
          
        elif(Bonus==4):
            
            Bonus_4 = 1
            
        elif(Bonus==5):
          
            Bonus_5 = 1
            
        elif(Bonus==6):
            
            Bonus_6 = 1
            
        else:
            
            Bonus_7 = 1
        
        Make=int(request.form['Make'])
        if(Make==2):
            Make_2 = 1
           
        elif(Make==3):
            
            Make_3 = 1
           
        elif(Make==4):
            
            Make_4 = 1
            
        elif(Make==5):
            
            Make_5 = 1
            
        elif(Make==6):
           
            Make_6 = 1
            
        elif(Make==7):
          
            Make_7 = 1
           
        elif(Make==8):
        
            Make_8 = 1
           
        else:
        
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