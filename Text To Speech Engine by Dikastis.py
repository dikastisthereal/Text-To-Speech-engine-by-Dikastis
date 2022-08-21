import pyttsx3 as tts
per = tts.init()
while True:
    Speech = input("Enter some text : ")
    per.say(Speech)
    per.runAndWait()