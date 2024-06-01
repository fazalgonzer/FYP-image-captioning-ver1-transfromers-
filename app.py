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


@app.route("/",methods=['GET'])
@cross_origin()
def home():
    captions="hello"
    return render_template('index.html',captions=captions)







@app.route("/upload",methods=['POST'])
@cross_origin()
def imageshow():
    file= None
    file=request.files["image"]

    if file:
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return render_template('index.html',image_path='D:\FYP caption Ver 1\FYP-image-captioning-ver1-transfromers-\uploads_for_user\img1.jpeg')
    
    
    return render_template('index.html',Error="image was not found")
    
        
   
    

if __name__ == "__main__":
    app.run(debug=True)