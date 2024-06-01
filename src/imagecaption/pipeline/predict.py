import os 
from transformers import AutoProcessor,BlipForConditionalGeneration
from PIL import Image 
from gtts import gTTS 
from playsound import playsound 




class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename
        self.captions= None

    def predict(self,audio:bool):
        #load_model
        model= BlipForConditionalGeneration.from_pretrained("artifacts\model_withbin")#yaha pr saved model ki file ki location deni h 
        processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base") # ye wese ka wese hi rehne de
        img = Image.open(self.filename)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs)
        captions=processor.decode(out[0], skip_special_tokens=True)
        self.captions=captions
        return captions
    def Play(captions):
          if os.path.exists('artifacts/Audio/2.mp3'):
                os.remove('artifacts/Audio/2.mp3')
          myobj = gTTS(text=captions, lang='en', slow=False)
            
          myobj.save('artifacts/Audio/2.mp3')
          playsound('artifacts/Audio/2.mp3')
            
        

      
          



 