# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #


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
#                            C++ Function Importing                            #
# ---------------------------------------------------------------------------- #


lib = cdll.LoadLibrary('./o_files/mainLib.so')

def get_response(number): # COMPLETED
    
    a = lib.get_response_so(number)
    return a


# ---------------------------------------------------------------------------- #
#                            TFLearn Model Functions                           #
# ---------------------------------------------------------------------------- #


def train_and_save_model(train): # COMPLETED

    if train:

        trainingInput = []
        expectedOutput = []
        allWords = []
        tagList = []
        wordLists = []
        wordLists_tags = []

        with open("STORAGE/intents.json") as file:
            data = json.load(file) # gets data from json file

        for intent in data["intents"]:

            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern) # seperates words in sentence
                allWords.extend(wrds)
                wordLists.append(wrds) # appending list of words
                wordLists_tags.append(intent["tag"]) # appending tag at same index of the list of words

            if intent["tag"] not in tagList: # making list of all the tags
                tagList.append(intent["tag"])

        allWords = [stemmer.stem(w.lower()) for w in allWords if w != "?"] # getting the stem of all of the words 
        allWords = sorted(list(set(allWords))) # sorting list of words and making sure there are no duplicates

        tagList = sorted(tagList) # sorting list of tagList

        tagList_empty = [0 for _ in range(len(tagList))] # addign a 0 to a list for every tag

        for x, wordList in enumerate(wordLists):
            
            bag = []

            stemmedWordList = [stemmer.stem(w.lower()) for w in wordList] # creating list of stemmed words for each specific set of words per tag

            for word in allWords: # for word in total words list
                if word in stemmedWordList: # if the word is in the word list for the specific tag
                    bag.append(1)
                else:
                    bag.append(0)

            outputTagList = tagList_empty[:] # creating a copy of the out_empty list
            outputTagList[tagList.index(wordLists_tags[x])] = 1 # getting the current tags index in tagList, and setting that value to a 1 in outputTagList

            trainingInput.append(bag) # adding the bag of words to list of all bags for training
            expectedOutput.append(outputTagList) # adding the output_row to total output
        
        trainingInput = numpy.array(trainingInput)
        expectedOutput = numpy.array(expectedOutput)

        NeuralNetwork = tflearn.input_data(shape=[None, len(trainingInput[0])]) # adding the input layer with a node for every possible word
        NeuralNetwork = tflearn.fully_connected(NeuralNetwork, 8) # adding a hidden layer with 8 nodes
        NeuralNetwork = tflearn.fully_connected(NeuralNetwork, 8) # adding a hidden layer with 8 nodes
        NeuralNetwork = tflearn.fully_connected(NeuralNetwork, len(expectedOutput[0]), activation="softmax") # adding an output layer with a node for every tag
        NeuralNetwork = tflearn.regression(NeuralNetwork) # optimizes I/O layers
        
        adaNN = tflearn.DNN(NeuralNetwork) # setting type of Neural Network

        pickle.dump((trainingInput, expectedOutput, allWords, tagList), open("STORAGE/pickle_files/TOWL.p", "wb")) # stores all the data for future usage

        adaNN.fit(trainingInput, expectedOutput, n_epoch=1000, batch_size=8, show_metric=True) # giving model input and proposed output and starting the training

        adaNN.save("STORAGE/tflearn_model/model.tfl") # saves the model for future use

        return (adaNN, allWords, tagList) # returns the model to make predictions and other lists for use elsewhere

    else:

        (training, output, allWords, tagList) = pickle.load(open("STORAGE/pickle_files/TOWL.p", "rb"))
    
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)

        adaNN = tflearn.DNN(net)

        adaNN.load("STORAGE/tflearn_model/model.tfl")

        return (adaNN, allWords, tagList)
    

# ---------------------------------------------------------------------------- #
#                                Other Functions                               #
# ---------------------------------------------------------------------------- #


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

def bag_of_words(s, words): # COMPLETED
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return numpy.array(bag)

def write_to_not_understood(line): # COMPLETED
    f = open("STORAGE/not_understood.txt", "w")
    f.write(line + "\n")


# ---------------------------------------------------------------------------- #
#                                   ADA Class                                  #
# ---------------------------------------------------------------------------- #


class ADA:

    def __init__(self, newModel = False):

        (self.model, self.words, self.tagList) = train_and_save_model(newModel)

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

            results = self.model.predict([bag_of_words(inpWithoutAda, self.words)])[0]
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
        