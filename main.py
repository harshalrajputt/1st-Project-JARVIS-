import speech_recognition as sr
import pyttsx3
import webbrowser




recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()    

def processcommand(command):
    command = command.lower()
    
    if "open youtube" in command:
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com")
        
    elif "open google" in command:
        speak("opening google")
        webbrowser.open("https://www.google.com")
        
    elif "open stack overflow" in command:
        speak("opening stack overflow")
        webbrowser.open("https://stackoverflow.com")
        
    elif "open github" in command:
        speak("opening github")
        webbrowser.open("https://github.com")
    
    elif "open facebook" in command:
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com") 
        
    elif "open twitter" in command:
        speak("opening twitter")
        webbrowser.open("https://www.twitter.com")    
    
        
    else:
        speak("sorry sir, i could not understand the command.")

if __name__ =="__main__":
    speak("initializing jarvis.....")
    
    while True:
        
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes sir, how can i help you?")
                # print("yes sir, how can i help you?")
                with sr.Microphone() as source:
                    print("Jarvis is listening...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processcommand(command)

     
        except Exception as e :
            print("jarvis error; {0}".format(e))
    

#to stop jarvis, press ctrl+c in the terminal
#to run the code, make sure you have installed the required librar0ies using pip