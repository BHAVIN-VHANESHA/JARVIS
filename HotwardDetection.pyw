from BasicFunctions import Listen
from Body import Start


def Wakeup():
    query = Listen()
    if 'Jarvis' in query:
        Start()
    else:
        pass


while True:
    Wakeup()
