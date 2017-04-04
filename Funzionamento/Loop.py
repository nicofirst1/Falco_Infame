import sys
import random
import os
import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space

from Funzionamento.Insulti import insulti

audio_dict={"118":"CQADBAADFgAD7UL4UuVtydPfvpEYAg"}

# creo una classe perche bho
class loop(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(loop, self).__init__(*args, **kwargs)

    # questa è la funzione per leggere i messaggi
    def on_chat_message(self, msg):

        # prendo alcuni parametri tra cui content_type
        content_type, chat_type, chat_id = telepot.glance(msg)

        # se il messaggio appena inviato è di testo allora vedo cosa c'è scritto
        if(content_type=="text"):
            message=msg.get("text").lower()

            if("loop" in message):
                command=message.split("loop")[1].split(",")
                if(len(command)!=2):
                    self.sender.sendMessage("Sintassi invalida!\nUso: \loop [frase da ripetere], [numero di ripetizioni] ")
                    return

                if(int(command[1])>20):
                    self.sender.sendMessage("Numero di ripetizioni troppo elevato! [massimo 20]")
                    return

                for i in range(1,int(command[1])+1):
                    self.sender.sendMessage(command[0])





