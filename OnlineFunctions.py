import requests
import wikipedia
import pywhatkit as kit
from bs4 import BeautifulSoup
from requests import get
from BasicFunctions import Speak, Listen


# from email.message import EmailMessage
# import smtplib
# from email import config


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]


def search_on_wikipedia(query):
    results = wikipedia.summary(query)
    return results


def play_on_youtube(video):
    kit.playonyt(video)


def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


# EMAIL = config("EMAIL")
# PASSWORD = config("PASSWORD")
#
#
# def send_email(receiver_address, subject, message):
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email['From'] = EMAIL
#         email.set_content(message)
#         s = smtplib.SMTP("smtp.gmail.com", 587)
#         s.starttls()
#         s.login(EMAIL, PASSWORD)
#         s.send_message(email)
#         s.close()
#         return True
#     except Exception as e:
#         print(e)
#         return False


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

'''
def currloc_temperature():
    IP_Address = get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + IP_Address + '.json'
    geo_reqeust = get(url)
    geo_data = geo_reqeust.json()
    city = geo_data['city']
    search = f"temperature in {city}"
    url_1 = f"https://www.google.com/search?q={search}"
    r = get(url_1)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    Speak(f"current {search} is {temp}")
'''


def Temperature():
    Speak("tell the name of place")
    city = Listen()
    url = f"https://www.google.com/search?q=temperature in {city}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temperature = data.find("div", class_="BNeawe").text
    Speak(f"the temperature outside is {temperature}")
