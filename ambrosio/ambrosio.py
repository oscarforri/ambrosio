#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import channels as ch
import actions as ac
import time
import yaml
import ppri

class Ambrosio(object):
    """Class for Ambrosio Personal Digital Butler

    Will run our house"""
    def __init__(self):
        super(Ambrosio, self).__init__()
        self.c1 = CommandList()

        self._get_config()
        self.channels = []
        self.channels.append(ch.TextChannel())
        self.channels.append(ch.TelegramChannel())

        self.actions = []
        self.actions.append(ac.MusicPlayer())

    def _get_config(self):
        with open("ambrosio.yaml") as f:
            self.cfg = yaml.load(f)

        print "Configuracio:"
        print self.cfg

    def next_command(self):
        try:
            return self.c1.next()
        except:
            return (None, None)

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.c1.append((chan, chan.get_msg()))

    def execute_command (self,command):
        print "will execute", command
        #Foreach Action in actions.
        # if is_for_you()
        #    action.do
        words = command.split()
        first_word = words[0]
        rest_words = words[1:]
        response = None

        for a in self.actions:
            if a.is_for_you(first_word):
                response = a.do(rest_words)
                break
        else:
            print "No t'entenc"

        return response

    def mainloop(self):
        #While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            chan, command = self.next_command()
            if command:
                #print command
                response = self.execute_command(command)
                chan.respond(response)
            time.sleep(1)
            self.update_channels()


if __name__ == "__main__":
    print "Here be dragons!"
    amb = Ambrosio()
    amb.mainloop()
