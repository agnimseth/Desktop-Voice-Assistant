import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os




engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
print("********* DESKTOP VOICE ASSISTANT ***************")
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning! SIR ")
    elif hour>=12 and hour<18:
        speak("good afternoon! SIR ")

    else:
        speak("good evening! SIR ")
    
    strTime=datetime.datetime.now().strftime("%H: %M: %S") 
    print(strTime) 
    speak(f" the time is {strTime}  ")
    speak(" this is your desktop assistant title queen  and  i am  created by Agnim Seth")

def takecommand():
    #its take command from user and reply..

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Excited to take command...  ")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said:", query)
        speak(query)
    
    except Exception as e:
        print(e)
        print("please give command again...")
        speak('please give command again...')
        return "None"
    return query
    

    


if __name__ == "__main__":
    wishMe()  
    while True:
        query = takecommand().lower()
    

    #logic for query which jarvis will give as output
        if 'wikipedia' in query :
            speak('searching wikipedia...wait for a second')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

        elif 'open google' in query:
            webbrowser.open("google.com")
        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com") 

        elif 'play music' in query:
            music_dic = 'F:\\songs'
            songs = os.listdir(music_dic)
            print(songs)
            os.startfile(os.path.join(music_dic, songs[0]))

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H: %M: %S") 
            print(strTime) 
            speak(f"the time is {strTime} ") 

        elif 'open code' in query:
            codepath="C:\\Users\\Agnim S\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open notepad' in query:
            codepath1="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codepath1)
        

    

        elif 'who are you' in query:
            print("i am your desktop asistant sir created by Agnim Seth.") 
            speak("i am your desktop asistant sir created by Agnim Seth.")
 
        elif 'who is little queen' in query:
            speak("this is me sir..your  desktop assistant created by APOORV mishra  , SOURABH baghel AND AGNIM seth IN THE GUIDENCE OF sir MR. LAL SINGH chouhan ")


        elif 'go and sleep' in query:
            print("LOVE YOU SIR BYE BYE")
            speak("love you tooo sir  bye bye...")  
            exit()    
          

