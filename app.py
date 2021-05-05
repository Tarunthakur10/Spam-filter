import numpy as np
import pickle
from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
model=pickle.load(open("model.pkl","rb"))

@app.route('/')
def hello_world():
    return 'Hello, World!'