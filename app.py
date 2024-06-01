from flask import Flask, render_template, request, redirect, url_for,  jsonify 

from flask_cors import CORS, cross_origin

import os 
from PIL import Image
from pathlib import Path
from imagecaption.pipeline.predict import PredictionPipeline
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads_for_user'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class Classifier():
    def __init__(self):
        self.filename=None
        self.classifier =None
    def making(self,img):
        self.filename=img
        self.classifier =PredictionPipeline(self.filename)
         
    
file_path=""     

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    captions=''
    return render_template('index.html',captions=captions)







@app.route("/upload",methods=['POST'])
@cross_origin()
def imageshow():
    file= None
    file=request.files["image"]

    if file:
           filename = file.filename
           file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
           clapp.making(file_path)
           file.save(file_path)
      
    
    return render_template('index.html',Error="image was not found")
    
        
@app.route('/predict',methods=['GET'])
@cross_origin()
def predict():
     captions =clapp.classifier.predict(False)
     return render_template('index.html',captions=captions)

     
     
    
    

if __name__ == "__main__":
    clapp=Classifier()
    app.run(debug=True)