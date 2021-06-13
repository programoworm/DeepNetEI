#Important Modules
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from flask import Flask,render_template, url_for ,flash , redirect
import joblib
from flask import request
import numpy as np
import tensorflow
import os
from flask import send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import tensorflow as tf

app=Flask(__name__,template_folder='template')

@app.route("/")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/covid")
def covid():
    return render_template("covid.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = load_model('diabetes.h5')
        result = loaded_model.predict(to_predict)
    elif(size==13):#Heart
        loaded_model = load_model("heart.h5")
        result =loaded_model.predict(to_predict)
    elif(size==9):#Covid
        loaded_model = load_model("covid.h5")
        to_predict=np.array(to_predict_list[:-1]).reshape(1,size-1)
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==8):#Daiabtes
            result = ValuePredictor(to_predict_list,8)
        elif(len(to_predict_list)==9):
            result = ValuePredictor(to_predict_list,9)
        elif(len(to_predict_list)==13):
            result = ValuePredictor(to_predict_list,13)
    #    return render_template("result.html", prediction=str(to_predict_list))
    if(np.round(result)==1):
        prediction='Sorry! You are maybe suffering'
        xyz= result
    else:
        prediction='Congrats! you are Healthy'
        xyz= result 
    return(render_template("result.html", prediction=prediction, xyz=xyz))

if __name__ == "__main__":
    app.run(debug=True)
