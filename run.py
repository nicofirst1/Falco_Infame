import sys
import random
import traceback
import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space

from bot import sticker_dict, TOKEN, nick_names

# creo una classe perche bho
class sticker_sender(telepot.helper.ChatHandler):

    def __init__(self, *args, **kwargs):
        super(sticker_sender, self).__init__(*args, **kwargs)
        self._dictionary = sticker_dict

    # questa è la funzione per leggere i messaggi
    def on_chat_message(self, msg):

        # prendo alcuni parametri tra cui content_type
        content_type, chat_type, chat_id = telepot.glance(msg)

        # se il messaggio appena inviato è di testo allora vedo cosa c'è scritto
        if(content_type=="text"):
            message=msg.get("text").lower()
            # tutti questi if hanno il compito di vedere se nel messaggio è presente uno dei soprannomi,
            #  se si invia uno sticker random associato
            if any(ext in message for ext in nick_names.get("tommaso")):
                self.sender.sendSticker(random.choice(self._dictionary.get("tommaso")))
            elif any(ext in message for ext in nick_names.get("roberta")):
                self.sender.sendSticker(random.choice(self._dictionary.get("roberta")))
            elif any(ext in message for ext in nick_names.get("roberto")):
                self.sender.sendSticker(random.choice(self._dictionary.get("roberto")))
            elif any(ext in message for ext in nick_names.get("salvatore")):
                self.sender.sendSticker(random.choice(self._dictionary.get("salvatore")))
            elif any(ext in message for ext in nick_names.get("federico")):
                self.sender.sendSticker(random.choice(self._dictionary.get("federico")))
            elif any(ext in message for ext in nick_names.get("clinciu")):
                self.sender.sendSticker(random.choice(self._dictionary.get("clinciu")))
            elif any(ext in message for ext in nick_names.get("nicolo")):
                self.sender.sendSticker(random.choice(self._dictionary.get("nicolo")))
            elif any(ext in message for ext in nick_names.get("edoardo")):
                self.sender.sendSticker(random.choice(self._dictionary.get("edoardo")))
            elif any(ext in message for ext in nick_names.get("chiara")):
                self.sender.sendSticker(random.choice(self._dictionary.get("chiara")))



# sta parte solo dio sa che fa
bot = telepot.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, sticker_sender, timeout=1000),
])
bot.message_loop(run_forever='Listening ...')

