import math
import re

#################################
# Log
#
# Class to store data from a
# log file
#
# members:
#   * table    - dictionary
#   * data     - array of numbers
#   * filename - name of log file
#################################
class Log:
    def __init__(self, filename):
        self.table = dict()
        self.data  = []
        self.filename = filename

    ##########################################
    # load
    ##########################################
    def load (self):

        logfile = open (self.filename, "r")             # open file
        begin = False
        for line in logfile:                            # for each line
            if begin:                                   # if in the data section
                if (re.match("^END", line)):            # stop if END reached
                    begin = False
                    continue
                l = line.split()                        # tokenize line
                d = []                                  # initialize empty list
                t = float (l.pop(0))                    # retrieve first number on the line
                d.append (t)                            # assign as first element of list
                d.append ([])                           # assign second element as empty list
                for num in l:
                    d[1].append (float(num))            # append the rest of the numbers to second list
                self.data.append (d)
            elif (re.match("^BEGIN", line)):
                begin = True
            else:
                l = line.split(":")
                self.table[ l[0] ] = l[1]
        logfile.close()                                 # close log file
