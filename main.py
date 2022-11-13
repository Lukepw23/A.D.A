# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #


from tkinter.tix import InputOnly
from Modules.voice_recognition.new_voice_recognition import ADA
from Modules.voice_recognition.speech_detection import recognize_speech_from_mic


# ---------------------------------------------------------------------------- #
#                              Main Loop Function                              #
# ---------------------------------------------------------------------------- #


def main_loop():

    train = input("Train Ada? (y/n) : ")

    if (train == "y"):
        train = True
    else:
        train = False

    ada = ADA(train)
    shutdown = False
    isBooted = False

    while not shutdown:

        inp = recognize_speech_from_mic()

        out = ada.get_predicted_response(inp)
        print(inp)
        if (out == "shutdown") or (out == "shut down"):
            print("shutting down")
            shutdown = True

        elif (out == "boot"):

            if not isBooted:

                bootOut = ada.boot()
                if (bootOut == "shutdown"):
                    shutdown = True
                elif (bootOut == "True"):
                    isBooted = True
            
            else:

                print("\n" + "ADA : " + "Already booted" + "\n")
                ada.tts_output("Already booted")

        elif (out != ""):

            if isBooted:

                print("\n" + "ADA : " + out + "\n")
                ada.tts_output(out)

            else:

                print("\n" + "ADA : " + "please boot" + "\n")
                ada.tts_output("please boot")

        

# ---------------------------------------------------------------------------- #
#                                   Main Call                                  #
# ---------------------------------------------------------------------------- #


main_loop()