__author__ = 'Bartek'


class Logger(object):
    def __init__(self, filename='log.txt'):
	self.filename = filename

    def log(message):
	    with open(self.filename,"a") as myfile:
		    myfile.write(time.ctime() + ": " + message + "\n")



