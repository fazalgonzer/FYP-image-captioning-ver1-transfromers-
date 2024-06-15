from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import json 
def accuracy_score(predict, actual):
    embed=HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
    predict_e=embed.embed_query(predict)
    accuracy_e=embed.embed_query(actual)
    similarity = cosine_similarity([predict_e], [accuracy_e])
    return similarity




#accuracy Score 
with open('accuracy_score\\anns.json', 'r') as file:
    # Load the data from the file
    data = json.load(file)

anns=[]

for i in range(0,100):
   anns.append(data[i][0]['caption'])



# Gen caption text 




with open('accuracy_score\caps_gen.txt', 'r') as file:
    # Load the data from the file
    gen_cap = file.readlines()
gen_cap=[line.strip() for line in gen_cap]


x=accuracy_score(gen_cap,anns)
print(x)
