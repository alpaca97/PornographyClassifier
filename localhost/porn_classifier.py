import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.layers import Activation, Dropout
import string
import json
from keras.models import model_from_json
def init(): 
	vocab = [x for x in string.ascii_lowercase] + [x for x in string.punctuation] + [x for x in string.digits]
	vocab.append(' ')
	vocab.append('END')
	vocab.append('specialchar')
	vocab = set(vocab)
	char_index = dict((c, i) for i, c in enumerate(vocab))
	return(char_index,vocab)

char_index,vocab=init()
title = raw_input("Please enter title: ")  # Python 2


 # load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")



def encodeTitle(title): 
  int_encoded = [char_index[char] if char in vocab else char_index['specialchar'] for char in title.lower()]
  if (len(title)<50):
    for i in range(50-len(title)):
      int_encoded.append(char_index["END"])

  onehot_encoded = []
  for value in int_encoded[:50]:
    letter = [0 for _ in range(len(vocab))]
    letter[value] = 1
    onehot_encoded.append(letter)
   	
  return(onehot_encoded)
onehot_encodedTitle= encodeTitle(title)
preds = loaded_model.predict(np.asarray(onehot_encodedTitle).reshape(1,50,71))
print "Prediction is " , preds
#print(type(preds))
def verdict(preds):
  if ((preds[0,0]>0.6)&(preds[0,1]<0.4)):
    return "Bruh, that's porn"
  else: 
    return "continue on my friend"

print(verdict(preds))
