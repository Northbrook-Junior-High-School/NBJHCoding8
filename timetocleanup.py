import datetime
import gtts
import os
import pyttsx3
import time
from gtts import gTTS
from playsound import playsound

engine = pyttsx3.init()

hournow = time.strftime("%H")
minutenow = time.strftime("%M")
timenow = str(f"{hournow}:{minutenow}")
numdaynow = time.strftime("%w")
weekday = True

timenow = "09:16"
while weekday:
    hournow = time.strftime("%H")
    minutenow = time.strftime("%M")
    secondnow = time.strftime("%S")
    timenow = str(f"{hournow}:{minutenow}:{secondnow}")
    numdaynow = time.strftime("%w")
    #    timenow = "09:16"
    if timenow == "09:16:00" or timenow == "09:59:00" or timenow == "10:42:00" or timenow == "11:25:00" or timenow == "14:50:00":
        # convert this text to speech
        text = "time to clean up"
        # engine.say(text)
        # play the speech
        # engine.runAndWait()
        sound = gTTS(text=text, lang='en', slow=False)
        sound.save("timetocleanup.mp3")
        playsound("timetocleanup.mp3")
