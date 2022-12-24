# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #


import speech_recognition as sr
from gtts import gTTS
import os

import pyttsx3
converter = pyttsx3.init()
converter.setProperty('voice', "com.apple.speech.synthesis.voice.karen")

converter.setProperty('rate', 165)
# converter.setProperty('volume', 1)


# ---------------------------------------------------------------------------- #
#                                   Functions                                  #
# ---------------------------------------------------------------------------- #


def recognize_speech_from_mic(): # COMPLETED

    with sr.Microphone(device_index=0) as source:
        # sr.Recognizer().adjust_for_ambient_noise(source, duration=0.3)
        print("listening.....")
        audio = sr.Recognizer().listen(source)
        print("done listening")

    try:
        output = sr.Recognizer().recognize_google(audio)
        return output
    except sr.RequestError:
        return "did not understand"
    except sr.UnknownValueError:
        return "did not understand"
    
def text_to_speech(inputText): # COMPLETED

    converter.say(inputText)

    converter.runAndWait()


# ---------------------------------------------------------------------------- #
#                        C++ Speech Recognition Function                       #
# ---------------------------------------------------------------------------- #


def create_speech_output_file(fileNumber, speechRecOutput): # COMPLETED
    fName = "output_files/speechRecOutput_" + str(fileNumber)
    f = open(fName, "x")
    f.write(speechRecOutput)
    f.close()

def cpp_recognize_speech_from_mic(number, question): # COMPLETED

    haveOutput = False

    while not haveOutput:

        print("\n" + "AVA : " + question + "\n")
        text_to_speech(question)

        with sr.Microphone(device_index=0) as source:
            # sr.Recognizer().adjust_for_ambient_noise(source, duration=0.3)
            print("c++ listening.....")
            audio = sr.Recognizer().listen(source)
            print("c++ done listening")

        try:
            output = sr.Recognizer().recognize_google(audio)
            print(output)
            create_speech_output_file(number,output)
            haveOutput = True
        except sr.RequestError:
            print("\n" + "AVA : " + "did not understand" + "\n")
            text_to_speech("did not understand")
        except sr.UnknownValueError:
            print("\n" + "AVA : " + "did not understand" + "\n")
            text_to_speech("did not understand")  

