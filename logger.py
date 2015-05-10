import time

__author__ = 'Bartek'


class Logger(object):
    def __init__(self, filename='log.txt'):
        self.filename = filename

    def log(self, name):
        with open(self.filename, "a") as myfile:
            print(time.ctime() + ": " + name + "\n")
            myfile.write(time.ctime() + ": " + name + "\n")



