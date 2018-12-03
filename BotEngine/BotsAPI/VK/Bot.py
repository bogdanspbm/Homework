import vk_api
from threading import Thread
import time
import threading
import random

vk = vk_api.VkApi(
    token='119f058d4dbe935ae2a8e1e8246ea16d9aa65dc8c822b0bbc3c127d9ddada7d2bfb2bcf70c007e35547f8')


class VKBot(Thread):

    def __init__(self, bot=-1):
        Thread.__init__(self)
        self.bot = bot
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        bot = self.bot
        while True:
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
