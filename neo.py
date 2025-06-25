'''

1. Core Features (Must-Haves)
- Voice Activation - Wake word like 'Hey Jarvis' or 'Krish'
- Voice-to-Text - Understands your spoken commands
- Text-to-Speech - Replies in a realistic human voice
- Personal Memory - Remembers your name, likes, routines, friends, etc.
- Command History - Keeps log of past commands and actions
- Smart Greeting - Welcomes you with time-based messages, mood, weather, etc.
- Offline Basic Mode - Works even without the internet (for basic tasks)
2. System Control Features
- Open Apps - 'Open Chrome', 'Start VS Code', etc.
- Control Volume - Mute, increase/decrease system volume
- Control Brightness - Adjust screen brightness
- Take Screenshots - 'Take screenshot' and save
- System Status - 'How much battery?', 'Is WiFi connected?'
- Shutdown / Restart / Sleep - With confirmation to avoid accidents
3. Internet Features
- Search Anything - Google, Wikipedia, YouTube searches
- Get Weather - Real-time weather info of any location
- Get News - Latest headlines and news summaries
- Send Emails - Send emails via voice or typed commands
- Read Messages - Check emails, notifications (secure & optional)
- Play YouTube / Spotify - Play specific music or videos
- Currency / Time / Location Info - 'What time is it in Canada?' or '1 USD to INR?'
4. Smart Personalization + Memory
- Long-Term Memory - Remembers your birthday, preferences, tasks
- Task Reminders - 'Remind me to drink water at 5 PM'
Complete Feature List for AI Assistant (Jarvis-like)
- Daily Schedule - Shows your agenda for the day
- Save Notes - 'Take a note' - saves text or audio
- Ask About Past - 'What did I ask yesterday?' or 'What note I saved last week?'
5. Chat & Personality Features
- Casual Conversation - Can chat like a human when you're bored
- Jokes, Quotes, Facts - Uplifting and fun
- Mood Detection - Responds based on your tone or words
- Change Voice/Name - Choose how it sounds or what it's called
- Memory Reset (optional) - Can forget things you ask it to forget
6. AI & Learning Features
- Learn New Commands - Teach it new tasks through voice/text
- Detect Repetition - Suggests improvements in your habits
- AI Integration - Uses ChatGPT or LLMs for advanced tasks
- Language Translation - 'Translate this to Spanish'
- Image Captioning (optional) - Describe what's in an image you upload
7. Developer / Utility Tools
- Run Python Code - Execute simple Python scripts via voice
- Git Commands - Pull/push projects with voice (advanced only)
- Set Alarms / Timers - Countdown or scheduled alarms
- File Organizer - Clean and sort your messy folders
- System Cleanup - Disk info, memory usage, clear temp files (with care)
8. Security Features
- Voice Lock / Face Lock - Only responds to your voice/face (optional)
- Password Manager - Store and retrieve passwords securely
- End-to-End Encryption - Keeps your memory and data safe
Complete Feature List for AI Assistant (Jarvis-like)
- Self-Destruct Option - Erase memory/logs with one secret command
9. Fun Features (Optional)
- Play Games - 'Play rock paper scissors' or quiz games
- AI Drawing - Create simple AI images from words
- Storytelling - Tells stories, riddles, or bedtime tales
- Jarvis Mode - Switches to 'Iron Man' themed responses
- Custom Voices - Use celebrity-style voices (text-to-speech)
Bonus Suggestions
- Android App Sync - Connect your phone
- PDF/Text Reader - 'Read this file out loud'
- Camera Access - Face recognition and photo logging              



'''



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
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
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
    """Tells the current day"""
    day = datetime.datetime.today().strftime("%A")
    speak(f"Today is {day}")

def tell_time():
    """Tells the current time"""
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")

def tell_date():
    """Tells the current date"""
    today = datetime.datetime.now().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_wikipedia(topic):
    """Fetches summary from Wikipedia"""
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
    """Performs a Google search"""
    if query:
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        webbrowser.open(url)
        speak(f"Here are the search results for {query}")
    else:
        speak("Please specify what to search for.")

def play_youtube(song_name):
    """Searches for a song on YouTube"""
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
    """Fetches live weather update (requires API key)"""
    api_key = "your_openweather_api_key" 
    city = "Your_City"  

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
    """Opens commonly used websites"""
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
    return False

def jarvis_intro():
    """Introduces Jarvis"""
    speak("Hello, my name is neo. I am your AI assistant. How can I assist you?")

def main():
    jarvis_intro()
    while True:
        query = take_command()
        if query:
            if "open" in query:
                if not open_website(query):
                    speak("I can only open predefined websites.")
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



"""
wiki pedia 
who is 
what is 
how to make 

google search 
 search for python tutorials

 what's the time
 tell me time

 what's the date
 tell me the date

 what day is to day
 tell me the day

 open
 fb 
 geeks for geeks
 yt
 fb google

 stop
 exit
 bye




"""