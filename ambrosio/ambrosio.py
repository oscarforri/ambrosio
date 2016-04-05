#!/usr/bin/env python
# -*- coding: utf-8 -*-

from commandlist import CommandList
import time

class Ambrosio(object):
    """Class for Ambrosio Personal Digital Butler

    Will run our house"""
    def __init__(self):
        super(Ambrosio, self).__init__()
        self.c1 = CommandList()

    def next_command(self):
        try:
            return self.c1.next()
        except:
            return None


    def mainloop(self):
        #While True:
        #   command = get_command
        #   do_command(command)
        #   update
        while True:
            command = self.next_command()
            time.sleep(1)


if __name__ == "__main__":
    print "Here be dragons!"
