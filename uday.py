import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from requests import get
import pyjokes
import pywhatkit
import pyowm
from PIL import ImageGrab
import pyautogui

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    """Function to speak the given text"""
    engine.say(text)
    engine.runAndWait()

def wish_me():
    """Function to wish the user based on the time of the day"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning,uday Master")
    elif 12 <= hour < 18:
        speak("Good afternoon, udayMaster")
    else:
        speak("Good evening,uday Master")
    speak("How can I help you?")

def take_command():
    """Function to take voice command from the user"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return None
    return query.lower()

def update_weather(city, temperature):
    """Function to simulate updating weather information (not real update)"""
    speak(f"Updating weather information for {city} to {temperature} degrees Celsius.")

if __name__ == "__main__":
    speak("Preparing T.E.S.L.")
    wish_me()

    while True:
        query = take_command()

        if query is None:
            continue

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'open reddit' in query:
            webbrowser.open("https://www.reddit.com")

        elif 'open notepad' in query:
            os.system("notepad.exe")

        
        elif 'the time' in query:
            str_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"Sir, the time is {str_time}")

        elif 'open my project' in query:
            vs_code_path = "C:\\Users\\uday kumar\\onedrive\\Local\\Programs\\Microsoft VS Code\\uday.py"
            os.startfile(vs_code_path)

        elif 'thank you' in query or 'thanks' in query:
            speak("You're welcome, Master!")
            break

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open whatsapp' in query:
            whatsapp_path = "C:\\Users\\uday\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            try:
                os.startfile(whatsapp_path)
            except FileNotFoundError:
                speak("Sorry, I couldn't find WhatsApp on your system.")
            except Exception as e:
                speak(f"An error occurred while trying to open WhatsApp: {str(e)}")

        
        elif 'my ip address' in query:
            ip_address = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip_address}")
            print(f"IP Address: {ip_address}")

        elif 'good morning' in query:
            speak("Good morning!")

        elif 'good evening' in query:
            speak("Good evening!")

        elif 'who are you' in query:
            speak("I am T.E.S.L, your virtual assistant.")

        elif 'favorite color' in query:
            speak('My favorite color is red.')

        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'search' in query:
            search_query = query.replace('search', '')
            pywhatkit.search(search_query)

        elif 'set timer' in query:
            timer_duration = query.replace('set timer', '').strip()
            try:
                time_seconds = int(timer_duration)
                speak(f"Setting timer for {time_seconds} seconds.")
                pywhatkit.timer(time_seconds)
            except ValueError:
                speak("Please specify a valid duration for the timer.")

        elif 'capture screenshot' in query:
            screenshot = pyautogui.screenshot()
            screenshot.save("screenshot.png")
            speak("Screenshot captured.")

        elif 'weather' in query:
            speak("Please provide the city name.")
            city = take_command()
            temperature = 89  # Simulated temperature update
            update_weather(city, temperature)

        else:
            speak("I'm not sure about that. Can you please repeat?")
