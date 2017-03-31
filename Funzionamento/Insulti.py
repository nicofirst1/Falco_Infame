import sys
import random
import os
import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space


path=os.path.dirname(os.path.abspath(__file__)).split("Funzionamento")[0]+"/files/insulti.txt"


with open(path) as file:
    insulti_list=file.readlines()

# creo una classe perche bho
class insulti(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(insulti, self).__init__(*args, **kwargs)

    # questa è la funzione per leggere i messaggi
    def on_chat_message(self, msg):

        # prendo alcuni parametri tra cui content_type
        content_type, chat_type, chat_id = telepot.glance(msg)

        # se il messaggio appena inviato è di testo allora vedo cosa c'è scritto
        if(content_type=="text"):
            message=msg.get("text").lower()

            if("insulta" in message):
                da_insultare=message.split("insulta")[1]
                insluto=da_insultare+" , "+random.choice(insulti_list)
                self.sender.sendMessage(insluto)





