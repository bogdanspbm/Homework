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
        ids = []

        while True:
            print('...')

            if not self.active:
                break

            telegarm_bot.get_updates(new_offset)

            last_update = telegarm_bot.get_last_update()

            for event in bot.bot_blueprints[bot.CurrentBP].funcs:
                if event.type == 'event':
                    for id in ids:
                        res = event.calculate_event(id)
                        if res != None and res != '':
                            print(str(id) + ' ' + res)
                            telegarm_bot.send_message(id,
                                                      res)


            if last_update != None:

                last_update_id = last_update['update_id']
                last_chat_text = last_update['message']['text']
                last_chat_id = last_update['message']['chat']['id']
                ids.append(last_chat_id)
                if bot.users_id.count(last_chat_id) == 0:
                    bot.users_id.append(last_chat_id)
                last_chat_name = last_update['message']['chat']['first_name']
                res = bot.bot_blueprints[
                    bot.CurrentBP].find_output_by_input(last_chat_text,last_chat_id)
                telegarm_bot.send_message(last_chat_id, res)
                print(res)

                new_offset = last_update_id + 1
