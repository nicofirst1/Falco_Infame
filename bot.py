from Funzionamento.Audio import run_audio
from Funzionamento.Insulti import run_insulti
from Funzionamento.Sticker import run_sticker

TOKEN = "259879078:AAHmqrSCT8B8O8PPN2us_cn01PruR50Ispo"

sticker_bot=run_sticker(TOKEN)
insulti_bot=run_insulti(TOKEN)
audio_bot=run_audio(TOKEN)


if False:
    insulti_bot.message_loop(run_forever='Listening ...')
if False:
    insulti_bot.message_loop(run_forever='Listening ...')
if True:
    insulti_bot.message_loop(run_forever='Listening ...')



