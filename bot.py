import telepot
from telepot.delegate import pave_event_space, per_chat_id, create_open

from Funzionamento.Audio import audio
from Funzionamento.Insulti import  insulti
from Funzionamento.Sticker import sticker_sender

TOKEN = "259879078:AAHmqrSCT8B8O8PPN2us_cn01PruR50Ispo"

bot = telepot.DelegatorBot(TOKEN, [
        pave_event_space()(
            per_chat_id(), create_open, sticker_sender, timeout=100),
        pave_event_space()(per_chat_id(), create_open, insulti, timeout=100),
    pave_event_space()(per_chat_id(), create_open, audio, timeout=100)
    ])

bot.message_loop(run_forever="listening ...")