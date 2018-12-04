from BotEngine.BotsAPI.Telegram.BotHandler import BotHandler
import datetime
import sys
from threading import Thread
import threading



class TelegramBot(Thread):

    def __init__(self, bot=-1):
        Thread.__init__(self)
        self.bot = bot
        self.active = True

    def run(self):
        telegarm_bot = BotHandler(
            self.bot.tel_token)
        new_offset = None
        bot = self.bot

        while True:
            print('...')

            if not self.active:
                break

            telegarm_bot.get_updates(new_offset)

            last_update = telegarm_bot.get_last_update()

            if last_update != None:

                last_update_id = last_update['update_id']
                last_chat_text = last_update['message']['text']
                last_chat_id = last_update['message']['chat']['id']
                last_chat_name = last_update['message']['chat']['first_name']

                telegarm_bot.send_message(last_chat_id, bot.bot_blueprints[
                    bot.CurrentBP].find_output_by_input(last_chat_text))

                new_offset = last_update_id + 1
