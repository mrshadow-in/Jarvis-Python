#Function
import datetime
import webbrowser
from Speak import Say
import pyjokes
import urllib
#2 Types

#1 - Non Input
#eg: Time , Date , Speedtest

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def Jokes():
    joke = pyjokes.get_joke()
    Say(joke)

def yt():
    webbrowser.open(url='https://youtube.com')

def facebook():
    webbrowser.open(url='https://facebook.com')

def xite():
    webbrowser.open(url='https://xitenodes.com')

def NonInputExecution(query):

    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()
    
    elif "jokes" in query:
        Jokes()
    
    elif "yt" in query:
        yt()
    
    elif "youtube" in query:
        yt()

    elif "fb" in query:
        facebook()

    elif "facebook" in query:
        facebook()
#2 - Input
#eg - google search , wikipedia

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name)
        Say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        import pywhatkit
        pywhatkit.search(query)

    elif "play" in tag:
        name = str(query).replace("play","")
        import pywhatkit
        pywhatkit.playonyt(query)

