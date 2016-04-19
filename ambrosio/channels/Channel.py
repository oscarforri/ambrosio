class Channel(object):
    """Channelclass"""
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name
    def respond(self, response):
        print "RESPONSE: ", response
