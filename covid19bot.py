from datetime import datetime
from sqlite3 import Date
from telegram.ext import Updater, CommandHandler,  MessageHandler, Filters
import requests
API_KEY="5182649982:AAETC5kZReAApasUGiVQTxqktjTn5jIHxAo"
updater=Updater(token=API_KEY)
dispatcher=updater.dispatcher
updater.start_polling()

greeting_array=["Hello","Hi","Hey","hello","hi","hey"]
def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Hello, how are you?")

hello_handler=CommandHandler(greeting_array,hello)
dispatcher.add_handler(hello_handler)

def electricity(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="https://www.youtube.com/watch?v=VnnpLaKsqGU")

electricity_handler=CommandHandler("learn_electric",electricity)
dispatcher.add_handler(electricity_handler)

#https://api.covid19api.com/summary
def summary(update,context):
    response=requests.get("https://api.covid19api.com/summary")
    if response.status_code==200:
        print("getting...")
        data=response.json()
        date=data["Date"][0:10]
        answer=f"Coivd19 summary as of {date}: \n"
        print(date)
        print(data["Global"])
        for att,val in data["Global"].items():
            if att not in["Date","NewRecovered","TotalRecovered"]:
                print(att,":",val)
                answer+=att+":"+str(val)+"\n"
        answer+="-----------------------------------------------------------------\n"
        # print(data["Countries"][77])
        dictIndia=dict(data["Countries"][77])
        print(dictIndia)
        for inatt, inval in dictIndia.items():
            if inatt not in["Date","NewRecovered","TotalRecovered","ID","Slug","CountryCode","Premium"]:
                answer+=inatt+":"+str(inval)+"\n"
        context.bot.send_message(chat_id=update.effective_chat.id,text=answer)
    else:
        print("error somthing has gone wrong")
        context.bot.send_message(chat_id=update.effective_chat.id,text="error somthing has gone wrong")
summary_handler=CommandHandler("summary",summary)
dispatcher.add_handler(summary_handler)


def unknown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Sorry I cant do that")

unknown_handler=MessageHandler(Filters.command,unknown)
dispatcher.add_handler(unknown_handler)