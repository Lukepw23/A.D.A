import json
import os
import pickle
from ctypes import cdll
import nltk
import numpy
import tflearn
from Modules.voice_recognition.speech_detection import recognize_speech_from_mic, text_to_speech
from nltk.stem.lancaster import LancasterStemmer
import time

stemmer = LancasterStemmer()

# ---------------------------------------------------------------------------- #

lib = cdll.LoadLibrary('./o_files/mainLib.so')

def get_response(number): # COMPLETED
    
    a = lib.get_response_so(number)
    return a

def get_output_from_TS_file(fileNumber): # COMPLETED
    fName = "output_files/TSoutput_" + str(fileNumber)
    f = open(fName)
    line = f.readline()
    f.close()
    os.remove(fName)
    return line

def create_TS_output_file(fileNumber, tag, sentence): # COMPLETED
    fName = "output_files/TSoutput_" + str(fileNumber)
    f = open(fName, "x")
    line = tag + ':' + sentence
    f.write(line)
    f.close()

def cpp_call(fileNumber, tag, sentence): # COMPLETED
    create_TS_output_file(fileNumber, tag, sentence)
    get_response(fileNumber)
    return get_output_from_TS_file(fileNumber)

def write_to_not_understood(line): # COMPLETED
    f = open("STORAGE/not_understood.txt", "w")
    f.write(line + "\n")

# ---------------------------------------------------------------------------- #

def train_basic_model():

    allWords = []

    with open("new_intents.json") as f:
        intentsFile = json.load(f)
    
    for intent in intentsFile["intents"]:
        for pattern in intent["patterns"]:
            for sentence in pattern["sentences"]:
                sWords = nltk.word_tokenize(sentence)
                allWords.extend(sWords)
    
    allWords = [stemmer.stem(w.lower()) for w in allWords if w != "?"]
    allWords = sorted(list(set(allWords)))

train_basic_model()

# ---------------------------------------------------------------------------- #

class ADA:

    def __init__(self, newModel = False):

        (self.model, self.words, self.tagList) = train_basic_model(newModel)
        pass

    def bag_of_words(self, s): # COMPLETED
        bag = [0 for _ in range(len(self.words))]

        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(self.words):
                if w == se:
                    bag[i] = 1
                
        return numpy.array(bag)

    def get_predicted_response(self, userInput): # COMPLETED

        print("Proccessing...")

        inpLower = userInput.lower()
        
        if (userInput == "did not understand"):
            
            print("Done Proccessing")
            return ""

        elif (inpLower == "shutdown") or (inpLower == "shut down"):
            
            print("Done Proccessing")
            return "shutdown"

        if ("ada" in inpLower) or ("aida" in inpLower):

            inpWithoutAda = ""

            inpWords = nltk.word_tokenize(inpLower)

            for i, word in enumerate(inpWords):
                if (word != "ada") and (word != "aida"):
                    inpWithoutAda += word

                    inpWithoutAda += " " if i != (len(inpWords)-1) else ""
            
            if inpWithoutAda[len(inpWithoutAda)-1] == " ":
                inpWithoutAda = inpWithoutAda[:-1]

            results = self.model.predict([self.bag_of_words(inpWithoutAda)])[0]
            results_index = numpy.argmax(results)

            if results[results_index] > 0.875:

                #print("Done Proccessing")
                return cpp_call(1, self.tagList[results_index], inpWithoutAda)
                    
            else:

                write_to_not_understood(userInput)
                #print("Done Proccessing")
                return "I do not Understand"
        
        else:

            #print("Done Proccessing")
            return ""

    def tts_output(self, inp): # COMPLETED
        
        text_to_speech(inp)

    def boot(self): # COMPLETED

        while True:

            print("\n" + "ADA : " + "Access code" + "\n")
            self.tts_output("Access code")

            code = recognize_speech_from_mic()

            if (code == "2163" or code == "to 163" or code == "too 163"):
                print("\n" + "ADA : " + "Access granted" + "\n")
                self.tts_output("Access granted")
                return "True"
            
            elif (code == "shutdown"):
                return "shutdown"

            else:
                print("\n" + "ADA : " + "invalid code" + "\n")
                self.tts_output("invalid code")
        