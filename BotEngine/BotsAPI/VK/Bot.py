import vk_api
from threading import Thread
import time
import threading
import random


class VKBot(Thread):

    def __init__(self, bot=-1):
        Thread.__init__(self)
        self.bot = bot
        self.vk = vk_api.VkApi(
            token=self.bot.vk_token)

        self.active = True

    def run(self):
        vk = self.vk
        bot = self.bot
        ids = []
        while True:
            if not self.active:
                break

            for event in bot.bot_blueprints[bot.CurrentBP].funcs:
                if event.type == 'event':
                    for id in ids:
                        res = event.calculate_event(id)
                        if res != None and res != '':
                            vk.method('messages.send',
                                      {'peer_id': id,
                                       'random_id': random.randrange(0,
                                                                     1000000),
                                       'message': res})

            message = vk.method('messages.getConversations',
                                {'offset': 0, 'counte': 20,
                                 'filter': 'unread'})
            if message['count'] >= 1:
                id = message['items'][0]['last_message']['from_id']
                ids.append(id)
                body = message['items'][0]['last_message']['text']
                if body != '':
                    res = bot.bot_blueprints[
                        bot.CurrentBP].find_output_by_input(body, id)
                    if res != None:
                        vk.method('messages.send',
                                  {'peer_id': id,
                                   'random_id': random.randrange(0, 1000000),
                                   'message': res})

        time.sleep(1)
