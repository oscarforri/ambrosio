import telepot

class Channel(object):
    """Channelclass"""
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name
    def respond(self, response):
        print "RESPONSE: ", response

class TextChannel(Channel):
    """channel class read commands  from file"""
    def __init__(self, name="TextChannel"):
        super(TextChannel, self).__init__(name)
        self.messages = []
        with open("messages.txt", "r") as f:
            for line in f:
                self.messages.append(line)

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0


class AmbrosioBot(telepot.Bot):
    """AmbrosioBot is my telgram bot"""
    def __init__(self, token):
        super(AmbrosioBot, self).__init__(token)
        self.clist = None

    def set_list(self,clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id, = telepot.glance(msg)
        if content_type == 'text':
            command =msg['text']
            if self.clist is not None:
                self.clist.append(command)


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
