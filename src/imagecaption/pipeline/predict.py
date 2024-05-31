import os 
from transformers import AutoProcessor,BlipForConditionalGeneration #inko pip install krke ssolve krna h 
from PIL import Image#inko pip install krke ssolve krna h 
from gtts import gTTS#inko pip install krke ssolve krna h 
from playsound import playsound#inko pip install krke ssolve krna h  
#phir import hongi wrna nahi 



class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename

    def predict(self,audio:bool):
        #load_model
        model= BlipForConditionalGeneration.from_pretrained("artifacts\model_withbin")#yaha pr saved model ki file ki location deni h 
        processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base") # ye wese ka wese hi rehne de
        img = Image.open(self.filename)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs)
        captions=processor.decode(out[0], skip_special_tokens=True)
        if audio== True:
            print(captions)
            myobj = gTTS(text=captions, lang='en', slow=False)
            if not os.path.exists:
                myobj.save('artifacts/Audio/2.mp3')
                playsound('artifacts/Audio/2.mp3')
            return captions 
        else:
            print(captions)
            return captions



 