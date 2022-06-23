from flask import Flask, render_template, request

import pickle
import numpy as np

from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_model.pkl', 'rb'))
@app.route('/')
def Home(): 
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        print(request)
        a = float(request.form['perimeter_mean'])
        b = float(request.form['concave points_mean'])
        c = float(request.form['radius_worst'])
        d = float(request.form['perimeter_worst'])
        e = float(request.form['concave points_worst'])
        
        prediction=model.predict([[a,b,c,d,e]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="sorry please enter the positive number")
        else:
            output = " have cancer" if output else " don't have cancer"
            # if output == 1:
            #     output = "have cancer"
            # else:
            #     output = "don't have cancer"
            return render_template('index.html',prediction_text="You {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)