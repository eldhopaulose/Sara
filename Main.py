from gtts import gTTS
import os
import speech_recognition as sr
import datetime
def Text_audio(speak):
    tts = gTTS(text=speak, lang='en')
    tts.save("hello.mp3")
    os.system("mpg321 hello.mp3")
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Text_audio("Good Morning!")

    elif hour>=12 and hour<18:
        Text_audio("Good Afternoon!")   

    else:
        Text_audio("Good Evening!")  

    Text_audio("I am Sara Sir. Please tell me how may I help you")   
wishMe()
def myCommand():
    Text_audio("Listening")                                                            
    r = sr.Recognizer()                                                                                  
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)                                                                        
    try: 
        MyText = r.recognize_google(audio, language='en-in') 
        MyText = MyText.lower() 
        print("You said " + MyText)
    except sr.UnknownValueError:
        Text_audio("Could not understand audio")
        print("Could not understand audio")
        myCommand()
myCommand()