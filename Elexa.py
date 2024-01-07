import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def Talk(text):
    engine.say(text) 
    engine.runAndWait()

def Take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
        command = Take_command()
        # print(command)
        if 'recite' in command:
            # song = command.replace('play','')
            song = "surah fatiha"
            Talk('playing')
            pywhatkit.playonyt(song)
        elif 'what is your name' in command:
            Talk('my name is alexa')
        elif 'how are you' in command:
            Talk('I am good thank you    how can i help you')
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            Talk('Now the time is' + time)
        elif 'tell' in command:
            person = command.replace('tell','')
            info = wikipedia.summary(person,1)
            print(info)
            Talk(info)
        elif 'girlfriend' in command:
            Talk('Sorry, you dont have any future girlfriend')
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            Talk(joke)
        # elif 'you are' in command:
        #     Talk('Please dont talk about myself')
        elif 'show me' in command:
            try:
                from googlesearch import search
            except ImportError:
                print("No module named 'google' found")
                
            # to search
            query = command.replace('show me','')
            Talk('showing the' + query)
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
        else:
            Talk('sorry, please say it again')
while True:
    run_alexa()
