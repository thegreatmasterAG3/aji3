import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',150)

def Speak(audio):
    print("")
    Assistant.say(audio)
    print(f" : {audio}")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()

# query = takecommand()

# if 'hello' in query:
#     Speak("hello sir")

# else:
#     Speak("no command found")

def TaskExe():

    def Music():
        Speak("Tell me the name of the Song!")
        musicname = takecommand()

        if 'akeli' in musicname:
            os.startfile("")

        elif 'blanko' in musicname:
            os.startfile("")

        else:
            pywhatkit.playonyt(musicname)

        Speak("Your Song Has Been Started!, Enjiy Sir!")

    def Whatsapp():
        Speak("Tell me the name of the person!")
        name = takecommand()

        if 'karan' in query:
            Speak("Tell me the Massage!")
            msg = takecommand()
            Speak("Tell me the time sir!")
            Speak("Time in Hour!")
            hour = int(takecommand())
            Speak("Time in minute!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+9779812105488",msg,hour,min,20)
            Speak("Ok sir, Sending Whatsapp Massage !")

        else:
            Speak("Tell me the phone number!")
            phone = int(takecommand())
            ph = '+977' + phone
            Speak("Tell me the Massage!")
            msg = takecommand()
            Speak("Tell me the time sir!")
            Speak("Time in Hour!")
            hour = int(takecommand())
            Speak("Time in minute!")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+9779812105488",ph,hour,min,20)
            Speak("Ok sir, Sending Whatsapp Massage !")

    def OpenApps():
        Speak("Ok Sir, Wait a second!")

        if 'code' in query:
            os.startfile("")

        elif 'telegram' in query:
            os.startfile("")

        


    while True:

        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir, I Am Jarvis.")
            Speak("Your Personal AI Assistant!")
            Speak("How May I Help You Sir?")

        elif 'how are you' in query:
            Speak("I am Fine Sir!")
            Speak("What about you sir?")

        elif 'you need a break' in query:
            Speak("Ok Sir , You Can Call Me Anytime !")
            break

        elif 'youtube search' in query:
            Speak("Ok Sir, This is what i found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Done Sir")

        elif 'google search' in query:
            Speak("This is what i found for your search sir!")
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            pywhatkit.search(query)
            Speak("Done Sir!")

        elif 'website' in query:
            Speak("Ok Sir, Launching...")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'launch' in query:
            Speak("Tell me the name of the website!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Done Sir!")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching Wikipedia.....")
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif 'whatapp massage' in query:
            Whatsapp()

        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('D:\\')
