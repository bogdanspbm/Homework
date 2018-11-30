from BotEngine.BotsAPI.Telegram.BotHandler import BotHandler
import datetime
from threading import Thread


class TelegramBot(Thread):

    def __init__(self, bot=-1):
        Thread.__init__(self)
        self.bot = bot

    def run(self):
        telegarm_bot = BotHandler(
            '736605353:AAEufeJOHvEpwxvTCd2pKPaSEIVZFVJ_rMU')
        greetings = ('здравствуй', 'привет', 'ку', 'здорово')
        now = datetime.datetime.now()
        new_offset = None
        today = now.day
        hour = now.hour
        bot = self.bot

        while True:
            telegarm_bot.get_updates(new_offset)
            print('...')

            last_update = telegarm_bot.get_last_update()

            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

            telegarm_bot.send_message(last_chat_id, bot.bot_blueprints[
                bot.CurrentBP].find_output_by_input(last_chat_text))

            new_offset = last_update_id + 1