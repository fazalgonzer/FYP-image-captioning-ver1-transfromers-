import os 
from transformers import AutoProcessor,BlipForConditionalGeneration 
from PIL import Image
from gtts import gTTS
from playsound import playsound



class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename

    def predict(self,audio:bool):
        #load_model
        model= BlipForConditionalGeneration.from_pretrained(os.path.join("artifacts","best_model_saved"))
        processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        img = Image.open(self.filename)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs)
        captions=processor.decode(out[0], skip_special_tokens=True)
        if audio== True:
            myobj = gTTS(text=captions, lang='en', slow=False)
            myobj.save(os.path.join("artifacts","Audio"))
            playsound(os.path.join("artifacts","Audio"))
            return captions
        else:
            return captions



        

        