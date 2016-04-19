from Channel import Channel
import telepot


class AmbrosioBot(telepot.Bot):
    """AmbrosioBot is my telgram bot"""
    def __init__(self, token):
        super(AmbrosioBot, self).__init__(token)
        self.clist = None
        self.chat_id = None

    def set_list(self,clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id, = telepot.glance(msg)
        if content_type == 'text':
            command =msg['text']
            if self.clist is not None:
                self.clist.append(command)
                self.chat_id = chat_id

    def respond(self, response):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, response)



class TelegramChannel(Channel):
    """channel class received commands from telegram"""
    def __init__(self, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(name)
        self.bot = AmbrosioBot("189884221:AAHls9d0EkCDfU0wgQ-acs5Z39aibA7BZmc")
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
                return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0


    def respond(self, response):
        if response is None:
            response = "Command not understand"
        self.bot.respond(response)
