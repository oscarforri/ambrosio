#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import channels as ch
import time

class Ambrosio(object):
    """Class for Ambrosio Personal Digital Butler

    Will run our house"""
    def __init__(self):
        super(Ambrosio, self).__init__()
        self.c1 = CommandList()
        self.channels = []
        self.channels.append(ch.TextChannel())

    def next_command(self):
        try:
            return self.c1.next()
        except:
            return None

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.c1.append(chan.get_msg())


    def mainloop(self):
        #While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            command = self.next_command()
            if command:
                print command
            time.sleep(1)
            self.update_channels()


if __name__ == "__main__":
    print "Here be dragons!"
    amb = Ambrosio()
    amb.mainloop()
