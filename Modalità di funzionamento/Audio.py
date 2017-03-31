import sys
import random
import os
import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space

from bot import TOKEN

audio_dict={"118":"CQADBAADFgAD7UL4UuVtydPfvpEYAg"}

# creo una classe perche bho
class audio(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(audio, self).__init__(*args, **kwargs)

    # questa è la funzione per leggere i messaggi
    def on_chat_message(self, msg):

        # prendo alcuni parametri tra cui content_type
        content_type, chat_type, chat_id = telepot.glance(msg)

        # se il messaggio appena inviato è di testo allora vedo cosa c'è scritto
        if(content_type=="text"):
            message=msg.get("text").lower()

            if("118" in message):
                self.sender.sendAudio(audio_dict.get("118"))





# sta parte solo dio sa che fa
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, audio, timeout=100),
])
bot.message_loop(run_forever='Listening ...')

