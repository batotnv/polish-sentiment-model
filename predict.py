from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras import models
from clean_text import clean_text

def predict(text):

    #possible classes
    classes = ["Neutral", "Positive", "Negative"]

    
    #string to array
    text_array = [text]
    
    #cleaning text
    text_array[0] = clean_text(text_array[0])

    #model load
    model = load_model('finalsentimentmodelv3.h5')
    #model.summary()

    #loading word index
    with open('finalwordindexv3.pkl', 'rb') as picklefile:
        word_index = pickle.load(picklefile)

    top_words = len(word_index)
    tokenizer = Tokenizer(num_words=top_words)
    tokenizer.word_index = word_index


    # converting text to integers
    test_sequences = tokenizer.texts_to_sequences(text_array)
    x_test = sequence.pad_sequences(test_sequences, maxlen=40)


    #results

    result = model.predict(x_test)
    # print(result)
    print("Neutral: %.2f%%" % (result[:,0]*100))
    print("Positive: %.2f%%" % (result[:,1]*100))
    print("Negative: %.2f%%" % (result[:,2]*100))
    # print(np.argmax(result[0]))

    #predicted class
    predicted_class = classes[np.argmax(result[0])]

    return predicted_class

predict("fajne fajne fajne")
