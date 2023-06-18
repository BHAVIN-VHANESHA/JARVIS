import openai
from dotenv import load_dotenv

# API key
file = open("API.txt", "r")
API = file.read()
file.close()
# print(API)

openai.api_key = API
load_dotenv()
completion = openai.Completion()


def Reply(question, chat_log=None):
    Filelog = open("chat_log.txt", "r")
    chat_log_templet = Filelog.read()
    Filelog.close()

    if chat_log is None:
        chat_log = chat_log_templet

    Prompt = f"{chat_log}You : {question}\n Jarvis : "
    response = completion.create(
        model="text-davinci-002",
        prompt=Prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0)
    ans = response.choices[0].text.strip()
    chat_log_templet_update = chat_log_templet + f"\nYou : {question} \nJarvis : {ans}"
    Filelog = open("chat_log.txt", "w")
    Filelog.write(chat_log_templet_update)
    Filelog.close()
    return ans


print(Reply("hi"))
