import telepot
from telepot.delegate import pave_event_space, per_chat_id, create_open

from Funzionamento.Audio import audio
from Funzionamento.Insulti import  insulti
from Funzionamento.Sticker import sticker_sender


def run(token,audio_bool=True,sticker_bool=True,insulti_bool=True):

    setting_lst=[]

    if(audio_bool): setting_lst.append(pave_event_space()(per_chat_id(), create_open, audio, timeout=100))
    if(sticker_bool): setting_lst.append(pave_event_space()(per_chat_id(), create_open, sticker_sender, timeout=100))
    if(insulti_bool): setting_lst.append(pave_event_space()(per_chat_id(), create_open, insulti, timeout=100))

    bot = telepot.DelegatorBot(token, setting_lst)
    bot.message_loop(run_forever="listening ...")