import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from google import genai

Recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "f24cc3b232f04103af2b3c093fb8964a"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ai(c):
    client = genai.Client(api_key="Enter the API key here")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=c
    )
    print(response.text)
    return response.text

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("www.facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("www.instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("www.linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("www.whatsapp.com")
    elif "open youtube" in c.lower():
        webbrowser.open("www.youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/everything?q=Apple&from=2026-06-06&sortBy=popularity&apiKey=f24cc3b232f04103af2b3c093fb8964a")
        # Check if the request was successful
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                print(article['title'])
    
    else:
        output = ai(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        
        print("Recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source,timeout=5,phrase_time_limit=10)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis is Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
       
