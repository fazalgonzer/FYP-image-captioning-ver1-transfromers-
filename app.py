from flask import Flask, render_template, request, redirect, url_for,  jsonify 

from flask_cors import CORS, cross_origin
import time 
import os 
from PIL import Image
from pathlib import Path
from imagecaption.pipeline.predict import PredictionPipeline
app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER











class Classifier():
    def __init__(self):
        self.filename=None
        self.classifier =None
    def making(self,img):
        self.filename=img
        self.classifier =PredictionPipeline(self.filename)
         
    
file_path=""     
captions=""

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    captions=''
    error=''
    return render_template('index.html',captions=captions,Error=error)







@app.route("/upload",methods=['POST'])
@cross_origin()
def imageshow():
    file= None
    file=request.files["image"]

    if file:
           filename = file.filename
           _, file_extension = os.path.splitext(filename)
           print(file_extension)
           if file_extension in ['.png', '.jpg', '.jpeg']:

                
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                if os.path.exists(file_path):
                    os.remove(file_path)
                clapp.making(file_path)
                file.save(file_path)
                return render_template('index.html',Error="File was uploaded sucessfully",image_path=file_path)
           else:
               return render_template('index.html',Error="unsupported file please upload jpg png ")
           
            
    else:
       return render_template('index.html',Error="image was not found or not supported type ")
    
end_audio=""  
        
@app.route('/predict',methods=['GET'])
@cross_origin()
def predict():
     try:
        start=time.process_time()
        captions =clapp.classifier.predict()
        end=time.process_time()-start
     except Exception as e:
        print("prediction failed")
        return render_template('index.html',Error="perdiction failed")
        raise e
     try:
        start_audio=time.process_time()
        clapp.classifier.Play(captions)
        end_audio=time.process_time()-start_audio
     except Exception as e:
         return render_template('index.html',Error="failed to save audio ")
     
         
     return render_template('index.html',captions=captions ,Error=f"time taken to processs {end}")

     
@app.route('/play', methods=['GET', 'POST'])
def play_audio():
    return render_template('audio.html',time_taken=end_audio)
    
    

if __name__ == "__main__": 
    clapp=Classifier()
   
    app.run(debug=True)