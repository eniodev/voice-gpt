import speech_recognition as SR
import pyttsx3
import pywhatkit
import wikipedia

jarvis = pyttsx3.init()
def jarvis_speak(content):
    jarvis.say(content)
    jarvis.runAndWait()
    print(content)


listener = SR.Recognizer()

def listen_to_user():
    try:
        jarvis_speak("Hey Buddy! I'm Tina, your virtual assistant.")
        
        with SR.Microphone() as source:
            jarvis_speak("How can I help you today ?")
            user_audio = listener.listen(source)
            user_input = listener.recognize_google(user_audio).lower()
            if "Jarvis" in user_input:
                print(user_input.upper())
                user_input = user_input.replace("Jarvis","")
    except:
        pass
    return user_input

command = listen_to_user()

if "Who is  " in command:
    try:
        command = command.replace("Who is  ", "")
        jarvis_speak("Playing "+ command)
        pywhatkit.playonyt(command)
    except:
        pass
    jarvis_speak(f"Looks like {command} ain't shit!")
    
else:
    try:
        jarvis_speak("Searching for : " + command)
        info = wikipedia.summary(command,1)
        jarvis_speak(info)
    except:
        pass
    jarvis_speak(f"Looks like {command} ain't shit!")