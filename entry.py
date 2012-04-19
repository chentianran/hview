import math
import re

#################################
# Entry
#
# Class to store data from a
# log file
#
# members:
#   * info     - dictionary
#   * data     - array of numbers
#   * filename - name of log file
#################################
class Entry:
    def __init__(self, filename):
        self.info = dict()
        self.data  = []
        self.filename = filename

    # Load the data from a file
    def load (self):

        entryfile = open (self.filename, "r")           # open file
        begin = False
        for line in entryfile:                          # for each line
            if begin:                                   # if in the data section
                if (re.match("^END", line)):            # stop if END reached
                    begin = False
                    continue
                if "," in line:
                    result = re.search ("[(](.*),(.*)[)]", line)
                    real = result.group(1)
                    imag = result.group(2)
                    self.data.append ([real, imag])
                else:
                    l = line.split()                        # tokenize line
                    self.data.append (l)
            elif (re.match("^BEGIN", line)):
                begin = True
            else:
                l = line.split(":")
                self.info[ l[0] ] = l[1]
        entryfile.close()                                  # close log file
