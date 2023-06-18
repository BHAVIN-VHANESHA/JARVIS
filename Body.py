import os
from pprint import pprint
import scipy as sp
from BasicFunctions import Speak, Listen, Exit, Greet
from PhoneTracker import Phonenumber_location_tracker
from OnlineFunctions import search_on_wikipedia, play_on_youtube, find_my_ip, search_on_google, send_whatsapp_message, \
    get_random_advice, get_random_joke
from OfflineFunctions import open_camera, open_notepad, open_discord, open_cmd, open_calculator, play_music, \
    screen_shot
import keyboard


# turning on jarvis
def Start():
    Greet()
    while True:
        query = Listen().lower()
        if 'bye' in query or 'i need a break' in query or 'talk to you later' in query:
            Exit()

        elif 'restart' in query:
            Start()

        elif 'open camera' in query:
            open_camera()

        elif 'close camera' in query:
            os.system('taskkill /f /im WindowsCamera.exe')

        elif 'open notepad' in query:
            open_notepad()

        elif 'close notepad' in query:
            os.system("taskkill /f /im Notepad.exe")

        elif 'open discord' in query:
            open_discord()

        elif 'close discord' in query:
            os.system("taskkill /f /im Discord.exe")

        elif 'open cmd' in query:
            open_cmd()

        elif 'close cmd' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'open calculator' in query:
            open_calculator()

        elif 'close calculator' in query:
            os.system("taskkill /f /im CalculatorApp.exe")

        elif 'ip address' in query:
            ip_address = find_my_ip()
            Speak(f'Your IP Address is {ip_address}.')
            # print(f'Your IP Address is {ip_address}')

        elif 'open wikipedia' in query:
            Speak('What do you want to search on Wikipedia, sir?')
            search_query = Listen().lower()
            results = search_on_wikipedia(search_query)
            Speak(f"According to Wikipedia, {results}")
            Speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'open youtube' in query:
            Speak('What do you want to play on Youtube, sir?')
            video = Listen().lower()
            play_on_youtube(video)
            if 'pause' in query:
                keyboard.press('space bar')
            elif 'play' in query:
                keyboard.press('space bar')
            elif 'forward' in query:
                keyboard.press('l')
            elif 'rewind' in query:
                keyboard.press('j')


        elif 'search on google' in query:
            Speak('What do you want to search on Google, sir?')
            query = Listen().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            Speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            Speak("What is the message sir?")
            message = Listen().lower()
            send_whatsapp_message(number, message)
            Speak("I've sent the message sir.")

        # elif "send an email" in query:
        #     Speak("On what email address do I send sir? Please enter in the console: ")
        #     receiver_address = input("Enter email address: ")
        #     Speak("What should be the subject sir?")
        #     subject = Listen().capitalize()
        #     Speak("What is the message sir?")
        #     message = Listen().capitalize()
        #     if send_email(receiver_address, subject, message):
        #         Speak("I've sent the email sir.")
        #     else:
        #         Speak("Something went wrong while I was sending the mail. Please check the error logs sir.")

        elif 'tell me a joke' in query:
            Speak(f"Hope you like this one sir")
            joke = get_random_joke()
            Speak(joke)
            # Speak("For your convenience, I am printing it on the screen sir.")
            # pprint(joke)

        elif "any advice" in query:
            Speak(f"Here's an advice for you sir")
            advice = get_random_advice()
            Speak(advice)
            # Speak("For your convenience, I am printing it on the screen sir.")
            # pprint(advice)

        # elif "trending movies" in query:
        #     Speak(f"Some of the trending movies are: {get_trending_movies()}")
        #     Speak("For your convenience, I am printing it on the screen sir.")
        #     print(*get_trending_movies(), sep='\n')
        #
        # elif 'news' in query:
        #     Speak(f"I'm reading out the latest news headlines, sir")
        #     Speak(get_latest_news())
        #     Speak("For your convenience, I am printing it on the screen sir.")
        #     print(*get_latest_news(), sep='\n')
        #
        # elif 'weather' in query:
        #     ip_address = find_my_ip()
        #     city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
        #     Speak(f"Getting weather report for your city {city}")
        #     weather, temperature, feels_like = get_weather_report(city)
        #     Speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
        #     Speak(f"Also, the weather report talks about {weather}")
        #     Speak("For your convenience, I am printing it on the screen sir.")
        #     print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'track' in query or 'track a mobile number' in query:
            Speak("Boss please enter the mobile number with country code")
            try:
                location, servise_prover, lat, lng = Phonenumber_location_tracker()
                Speak(
                    f"Boss the mobile number is from {location} and the service provider for the mobile number is {servise_prover}")
                Speak(f"latitude of that mobile nuber is {lat} and longitude of that mobile number is {lng}")
                print(location, servise_prover)
                print(f"Latitude : {lat} and Longitude : {lng}")
                Speak("Boss location of the mobile number is saved in Maps")
            except:
                Speak("Boss an unexpected error occured couldn't track the mobile number")

        elif "let's have some music" in query:
            play_music()


        elif 'screenshot' in query:
            screen_shot()
