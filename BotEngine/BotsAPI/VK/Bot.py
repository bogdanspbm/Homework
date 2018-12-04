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
        while True:
            if not self.active:
                break

            message = vk.method('messages.getConversations',
                                {'offset': 0, 'counte': 20,
                                 'filter': 'unread'})
            if message['count'] >= 1:
                id = message['items'][0]['last_message']['from_id']
                body = message['items'][0]['last_message']['text']
                if body != '':
                    vk.method('messages.send',
                              {'peer_id': id,'random_id':random.randrange(0,1000000), 'message': bot.bot_blueprints[
                                  bot.CurrentBP].find_output_by_input(body)})
        time.sleep(1)
