import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import requests
import re
from urllib.parse import quote_plus

def speak(text):
    """Converts text to speech"""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Takes voice input and converts it to text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=8)
            query = r.recognize_google(audio, language="en-in").lower().strip()
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Timeout: No voice detected.")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError:
            print("Speech recognition service unavailable.")
            return None

def tell_day():
    day = datetime.datetime.today().strftime("%A")
    speak(f"Today is {day}")

def tell_time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def tell_date():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_wikipedia(topic):
    try:
        if not topic:
            speak("Please provide a topic.")
            return
        speak(f"Searching Wikipedia for {topic}...")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("No information found on that topic.")
    except Exception:
        speak("There was an error fetching Wikipedia data.")

def google_search(query):
    if query:
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    else:
        speak("Please specify what to search for.")

def play_youtube(song_name):
    if song_name:
        search_query = quote_plus(song_name)
        html = requests.get(f"https://www.youtube.com/results?search_query={search_query}").text
        video_ids = re.findall(r"watch\?v=(\S{11})", html)
        if video_ids:
            video_url = f"https://www.youtube.com/watch?v={video_ids[0]}"
            webbrowser.open(video_url)
            speak(f"Playing {song_name} on YouTube")
        else:
            speak("Sorry, couldn't find the song on YouTube.")
    else:
        speak("Please provide a song name.")

def get_weather():
    api_key = "your_openweather_api_key"  # Replace with your OpenWeather API key
    city = "Your_City"  # Replace with your city
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url).json()
        if response["cod"] == 200:
            temp = response["main"]["temp"]
            weather_desc = response["weather"][0]["description"]
            speak(f"The current temperature in {city} is {temp} degrees Celsius with {weather_desc}.")
        else:
            speak("I couldn't fetch the weather details.")
    except Exception:
        speak("There was an error getting the weather update.")

def open_website(command):
    """Opens predefined or general websites"""
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "geeks for geeks": "https://www.geeksforgeeks.org",
        "instagram": "https://www.instagram.com",
        "snapchat": "https://www.snapchat.com"   
    }

    for site, url in websites.items():
        if site in command:
            speak(f"Opening {site}")
            webbrowser.open(url)
            return True

    # Dynamic domain support
    words = command.lower().split()
    if "open" in words:
        index = words.index("open")
        if index + 1 < len(words):
            domain = words[index + 1].replace(" ", "")
            url = f"https://www.{domain}.com"
            speak(f"Opening {domain}")
            webbrowser.open(url)
            return True

    speak("Sorry, I couldn't understand which website to open.")
    return False

def jarvis_intro():
    speak("Hello, my name is Neo. I am your AI assistant. How can I assist you?")

def main():
    jarvis_intro()
    while True:
        query = take_command()
        if query:
            if "open" in query:
                open_website(query)
            elif "day" in query and "date" not in query:
                tell_day()
            elif "time" in query:
                tell_time()
            elif "date" in query:
                tell_date()
            elif any(keyword in query for keyword in ["who is", "what is", "tell me about", "how to make"]):
                topic = re.sub(r"(who is|what is|tell me about|how to make)", "", query).strip()
                search_wikipedia(topic if topic else take_command())
            elif "search google for" in query:
                google_search(query.replace("search google for", "").strip())
            elif "play" in query:
                play_youtube(query.replace("play", "").strip())
            elif "weather" in query or "give me weather update" in query:
                get_weather()
            elif any(keyword in query for keyword in ["your name", "who are you", "introduce yourself"]):
                speak("My name is Jarvis. I am your AI assistant.")
            elif "bye" in query or "exit" in query or "stop" in query:
                speak("Goodbye! Have a great day.")
                break
            else:
                speak("I'm not sure what you mean. Please try again.")

if __name__ == "__main__":
    main()
