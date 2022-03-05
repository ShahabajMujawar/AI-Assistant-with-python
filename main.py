import camera as camera
import pyttsx3 as p  #it use to import the voices
import speech_recognition as sr   #it is use to import or convert speech to text
from youtube_auto import *
from selenium_web import *
from selenium_web import infow

engine = p.init()

#adjust the speed of saying
rate = engine.getProperty('rate')
engine.setProperty('rate',180)

#checking the voices provide by computer
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()  #runandwait module is used to used to comlete the sentence to finished.

r = sr.Recognizer()  #recognizer is use to recognize the user hardware

speak("hello sir i am your voice assistant. how are you?")

with sr.Microphone() as source:
    r.energy_threshold=10000 #here energy_threshold is use to get if voice is low pich
    r.adjust_for_ambient_noise(source,1.2) #ambient_noise is use to cancle the noice in background
    print("listening..")
    audio = r.listen(source)
    text = r.recognize_google(audio)  #here it capture the voice data and send to google api engine to convert it to text
    print(text)

#this if condicution get invocked when user ask the assistant what aboutyou?##
if "what" and "about" and "you" in text:
    speak("i am also having a good day sir")
speak("what can i do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000    #here energy_threshold is use to get if voice is low pich
    r.adjust_for_ambient_noise(source,1.2)   #ambient_noise is use to cancle the noice in background
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information related to which topic?")

    with sr.Microphone() as source:
        r.energy_threshold = 10000  # here energy_threshold is use to get if voice is low pich
        r.adjust_for_ambient_noise(source, 1.2)  # ambient_noise is use to cancle the noice in background
        print("listening..")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = infow()
    assist.get_info(infor)



elif "play" and "video" in text2:
    speak("you want to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # here energy_threshold is use to get if voice is low pich
        r.adjust_for_ambient_noise(source, 1.2)  # ambient_noise is use to cancle the noice in background
        print("listening..")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("opening {} in youtube".format(vid))
    speak("opening {} in youtube".format(vid))
    assist = music()
    assist.play(vid)