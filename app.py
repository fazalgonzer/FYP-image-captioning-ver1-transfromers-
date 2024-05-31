from flask import Flask, request ,render_template , jsonify
import os 
from flask_cors import CORS, cross_origin

from imagecaption.pipeline.predict import PredictionPipeline
os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL','en_US.UTF-8')

app= Flask(__name__)
CORS(app)


class ClientAPP:
    def __init__(self):
        self.filename="inputImage.jpg"
        self.classifier =PredictionPipeline(self.filename)

@app.route("/",methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')



#@app.route("/train",methods=['GET','POST'])
#@cross_origin()
#def trainRoute():
 #   os.system("python main.py")
  #  return "training done Succesfully"

@app.route("/predict",methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    
    result=clApp.classifier.predict()
    return jsonify(result)


if __name__ =="__main__":
    clApp=ClientAPP()
    app.run(host='0.0.0.0',port=80) 