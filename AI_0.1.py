import requests
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import requests
import pywhatkit
import pyautogui
import datetime
from playsound import playsound

from bs4 import BeautifulSoup



url="https://google.com"
timeout=5


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
  engine.say(audio)
  engine.runAndWait()



def wishme():
    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning..")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening..")

    speak("I am jarvise sir. How can i help you..")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        quary = r.recognize_google(audio, language='en-in')
        print(f"User said: {quary}\n")                                                                              

    except Exception as e:
        #print(e)

        print("Please try again.... ")
        #speak('please try again..')
        return "None"
    return quary


def Music():
    speak('tell me the song')
    musicname=takecommand()

    pywhatkit.playonyt(musicname)

    speak('your song is started. Enjoy sir..')

def Whatsapp():

    speak('Tell me the name of persion!')
    name=takecommand()
    
    if 'Ganesh'in name:
        speak('Tell me the message!')
        msg=takecommand()
        speak('Tell me the Time sir!')
        speak('Time in hour!')
        hour=int(input("Enter Hr:"))
        speak('Time in Minutes!')
        min=int(input("Enter Min :"))
        pywhatkit.sendwhatmsg('+917775945749', msg, hour, min,10)
        speak('sending whatsapp message')
    elif 'Nagma' in name:
         speak('Tell me the message!')
         msg=takecommand()
         speak('Tell me the Time sir!')
         speak('Time in hour!')
         hour=int(input("Enter Hr:"))
         speak('Time in Minutes!')
         min=int(input("Enter Min :"))
         pywhatkit.sendwhatmsg('+917821947086', msg, hour, min,10)
         speak('sending whatsapp message')
    else:
         speak('Tell me the number')
         phno=int(input("Enter Phno:"))
         ph='+91'+phno
         speak('Tell me the message!')
         msg=takecommand()
         speak('Tell me the Time sir!')
         speak('Time in hour!')
         hour=int(input("Enter Hr:"))
         speak('Time in Minutes!')
         min=int(input("Enter Min :"))
         pywhatkit.sendwhatmsg('+917821947086', msg, hour, min,10)
         speak('sending whatsapp message')


   



try:
    request=requests.get(url,timeout=timeout)
    print("connected")

    if __name__=="__main__":
        wishme()
    while True:
    #if 2:
        quary = takecommand().lower() 

        if 'wikipedia' in quary:
            speak('Searching wikipedia...')
            quary = quary.replace("wikipedia", "")
            results = wikipedia.summary(quary, sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in quary:
            speak('opening youtube...')
            print('opening youtube...')
            webbrowser.open("youtube.com")

        elif 'open google' in quary:
            speak('opening google...')
            print('opening google...')
            webbrowser.open("google.com")

        elif 'open instagram' in quary:
            speak('opening instagram...')
            print('opening instagram...')
            webbrowser.open("instgram.com")

        elif 'visual studio' in quary:
            speak('visual studio code...')
            print('visual studio code...')
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)

        elif 'SQL commad line' in quary:
            speak('opening sql commad line..')
            print('opening sql commad line..')
            codePath = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle Database 10g Express Edition"
            os.startfile(codePath)

        elif 'open file' in quary:
            print('opening File...')
            speak('openging File...')
            codePath="D:\\"
            os.startfile(codePath)

        elif 'play music' in quary:
            speak('playing music')
            print('playing music')
            music_dir = 'D:\\Saurabh\\SAURABH PER\\video\\My Songs'
            songs = os.listdir(music_dir)
           # print(songs)
            os.startfile(os.path.join(music_dir,songs[5]))
            #Music()

        elif 'time' in quary:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'take a break' in quary:
            speak("ok sir. you can call me any time..")
            break

        elif 'temperature' in quary:
            search = "temperature in masalga"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} in {temp}")
            speak(f"current {search} in {temp}")

        elif 'weather' in quary:
            search = "todays weather is"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f" {search} {temp}")
            speak(f" {search} {temp}")

        elif 'thank you' in quary:
            speak("your wellcome sir..")
            print("your wellcome sir..")

        elif 'hello' in quary:
            speak("hello sir..")
            print("hello sir..")

        elif 'how are you' in quary:
            speak('I am fine sir...')
            speak('what about you..')
            print('I am fine sir...')
            print('what about you..')
            
        elif 'about your self' in quary:
            speak("I'm shravan with artificial Technology ")
            print("I'm shravan with artificial Technology ")

        elif 'play song' in quary:
            #Music()
            speak('tell me the song')
            musicname=takecommand()
            pywhatkit.playonyt(musicname)
            speak('your song is started. Enjoy sir..')

        elif 'search' in quary:
            speak('This is i found')
            quary=quary.replace('search', ' ')
            pywhatkit.search(quary)
            speak('done sir....')

        elif 'website' in quary:
            speak('ok sir.')
            quary=quary.replace('jarvise','')
            quary=quary.replace(' website', '')
            web1=quary.replace('open ', '')
            quary=quary.replace(' ', '')
            web2='https://www.'+web1+'.com'
            webbrowser.open(web2)
            speak('opening sir..')

        elif 'whatsapp message' in quary:
            Whatsapp()

        elif 'open map' in quary:
            webbrowser.open('https://www.google.com/maps/place/Latur,+Maharashtra/@18.4031567,76.5319481,13z/data=!3m1!4b1!4m5!3m4!1s0x3bcf83bd7132cd29:0x83629bac5848da3e!8m2!3d18.4087934!4d76.5603828')
            speak('opening map')

        elif 'repeat my words'in quary:
            speak('speak sir')
            jj=takecommand()
            speak(f'you said:{jj}')
        
        elif'my location'in quary:
            speak('ok sir ,wait a second')
            webbrowser.open('https://www.google.com/maps/place/Rajarshi+Shahu+College,+Latur/@18.4019744,76.5713433,15.34z/data=!4m13!1m7!3m6!1s0x3bcf83bd7132cd29:0x83629bac5848da3e!2sLatur,+Maharashtra!3b1!8m2!3d18.4087934!4d76.5603828!3m4!1s0x3bcf8396336609e5:0xe06922ffa998a978!8m2!3d18.3985679!4d76.5796531')

        elif'set alarm' in quary:
            speak('Enter the time!')
            time=input(':Enter The Time :')

            while True:
                Time_Ac=datetime.datetime.now()
                now=Time_Ac.strftime('%H:%M:%S')

                if now == time:
                    speak('Time To Weakup Sir')
                    playsound('a1.mp3')
                    speak('Alarm Colsed!')

                elif now>time:
                    break
            
        elif'explain yourself' in quary:
            speak("I'm Jarvis  with artificial Technology. I include 15 differnt libraries. Which is helpfull for preforming differt task.currently i have included 25 different task.My speed is depend on your internet speed ")
            print("I'm Jarvis with artificial Technology. I include 15 differnt libraries. Which is helpfull for preforming differt task.currently i have included 25 different task .My speed is depend on your internet speed")
            
        else:
            print('Currently this command is unavailable')
            #speak('Currently this command is unavailable')

except Exception as e:
    print("Not Connected")
    speak("Please check your internet connection")       





        
