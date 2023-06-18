import os
import subprocess as sp
import pyautogui
import pywhatkit
from BasicFunctions import Listen, Speak

paths = {
    'notepad': "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2304.26.0_x64__8wekyb3d8bbwe\\Notepad"
               "\\Notepad.exe",
    'discord': "C:\\Users\\BHAVIN VHANESHA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord "
               "Inc\\Discord.lnk",
    'calculator': "C:\\Program Files\\WindowsApps\\Microsoft.WindowsCalculator_11.2210.0.0_x64__8wekyb3d8bbwe"
                  "\\CalculatorApp.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_calculator():
    sp.Popen(paths['calculator'])


def play_music():
    Speak("which song you want to play sir")
    music = Listen().lower()
    music_dir = r"C:\Users\BHAVIN VHANESHA\Music"
    songs = os.listdir(music_dir)
    if f'{music}.mp3' in songs:
        os.startfile(os.path.join(music_dir, f'{music}.mp3'))
    elif not f'{music}.mp3' in songs:
        pywhatkit.playonyt(music)
        Speak("enjoy sir")
    else:
        Speak("Boss an unexpected error occured")


def screen_shot():
    Speak("by which name i should save the screenshot")
    name = Listen()
    kk = pyautogui.screenshot()
    kk.save(rf"C:\Users\BHAVIN VHANESHA\OneDrive\Pictures\Screenshots\{name}.png")
    os.startfile(rf"C:\Users\BHAVIN VHANESHA\OneDrive\Pictures\Screenshots\{name}.png")
    Speak("here is your screenshot")
