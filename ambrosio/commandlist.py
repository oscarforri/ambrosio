

class CommandList(object):
    def __init__(self):
        super(CommandList, self).__init__()
        self.commands = []

    def next(self):
        return self.commands.pop(0) #Afegeixo per un estrem i surt per laltre.

    def append(self, command):
        self.commands.append(command)

    def length(self):
        return len(self.commands)
