# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Disptach method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")
# n=0
# while n<1 :
#     n=n+1

for a in range(2):
    a = input("write anything--")
    speaker.Speak(a)

# To stop the program press
# CTRL + Z