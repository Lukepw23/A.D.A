# ---------------------------------------------------------------------------- #
#                                    Imports                                   #
# ---------------------------------------------------------------------------- #


from tkinter.tix import InputOnly
from Modules.voice_recognition.new_voice_recognition import AVA
from Modules.voice_recognition.speech_detection import recognize_speech_from_mic


# ---------------------------------------------------------------------------- #
#                              Main Loop Function                              #
# ---------------------------------------------------------------------------- #


def main_loop():

    train = input("Train Ava? (y/n) : ")

    if (train == "y"):
        train = True
    else:
        train = False

    ava = AVA(train)
    shutdown = False
    isBooted = False

    while not shutdown:

        inp = recognize_speech_from_mic()

        out = ava.get_predicted_response(inp)
        print(inp)
        if (out == "shutdown") or (out == "shut down"):
            print("shutting down")
            shutdown = True

        elif (out == "boot"):

            if not isBooted:

                bootOut = ava.boot()
                if (bootOut == "shutdown"):
                    shutdown = True
                elif (bootOut == "True"):
                    isBooted = True
            
            else:

                print("\n" + "AVA : " + "Already booted" + "\n")
                ava.tts_output("Already booted")

        elif (out != ""):

            if isBooted:

                print("\n" + "AVA : " + out + "\n")
                ava.tts_output(out)

            else:

                print("\n" + "AVA : " + "please boot" + "\n")
                ava.tts_output("please boot")

        

# ---------------------------------------------------------------------------- #
#                                   Main Call                                  #
# ---------------------------------------------------------------------------- #


main_loop()