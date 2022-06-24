import opennre
import sys
import os
from transformers import logging
logging.set_verbosity_error()

#model = opennre.get_model('wiki80_bertentity_softmax')

def predict(text, subj1, subj2):
    model = opennre.get_model('wiki80_bertentity_softmax')
    h1 = text.find(subj1)
    h2 = h1+len(subj1)
    t1 = text.find(subj2)
    t2 = t1+len(subj2)

    res = model.infer({
    'text': text, 
    'h': {'pos': (h1, h2)}, 
    't': {'pos': (t1, t2)}
    })
    print(subj1, ' -> ' , subj2, " : ", res[0],  '(confidence = ',res[1],")")
    return ""+ subj1+ ' -> ' + subj+ " : "+ res[0]+  '(confidence = '+res[1]+")"

if __name__== "main":
    predict("Sergio lives in Paris and is quite content with his life of a royal heir", "Sergio", "Paris")