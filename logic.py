import time
import os


def clr():
    os.system('cls')


class Queue():

    def __init__(self):
        self.x = 0
        self.key = 0

    def add_number(self):
        self.x += 1
        return self.x
