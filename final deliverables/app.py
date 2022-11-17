import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("university.pkl", "rb"))

@app.route("/")
def home():
    return render_template('Demo2.html')

@app.route("/y_predict", methods = ["POST","GET"])
def y_predict():
    min1 = [290.0, 92.0, 1.0, 1.0, 1.0, 6.8, 1]
    max1 = [340.0, 120.0, 5.0, 5.0, 5.0, 9.92, 2]
    k = [float(x) for x in request.form.values()]
    print(k)
    p = []
    for i in range(7):
        l = (k[i]-min1[i])/(max1[i]-min1[i])
        p.append(l)
    prediction = model.predict([p])
    print(prediction)
    output = prediction[0]
    if output== False:
        return render_template("noChance.html", prediction_text="you dont have a chance")
    else:
        return render_template("chance.html", prediction_text="you have a chance")

if __name__ == "__main__":
    app.run(debug=True)
