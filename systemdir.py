import os
from log import Log
from soln import Soln

class Entry:
    def __init__(self):
        self.soln = None
        self.logs = {} 

    def __str__(self):
        retStr = self.soln.filename+ "\n\t"
        for k in self.logs.keys():
            retStr += k + " " + self.logs[k].filename + "\n\t"
        return retStr


class SystemDir:
    def __init__(self, systemDir):
        self.systemDir = systemDir
        self.entries = {}

        # read filenames and layout data 
        for fname in os.listdir(systemDir):
            
            if not self.validName(fname):
                print "Invalid filename: ", fname
                continue

            filePath = systemDir + '/' + fname
            fnameParts = fname.split('.')
            entryNum = fnameParts[-1]
            
            if fnameParts[0].startswith("log"): # log file
                logType = fnameParts[1]
                if not self.entries.has_key(entryNum): # entry not initialized
                    self.entries[entryNum] = Entry()
                self.entries[entryNum].logs[logType] = Log(filePath)   

            else:
                if not self.entries.has_key(entryNum):
                    self.entries[entryNum] = Entry()
                self.entries[entryNum].soln = Soln(filePath)


    def validName(self, fname):
        valid = True
        fnameParts = fname.split('.')
        #correct number of parts in filename
        if fnameParts[0] == 'log':
            valid = valid and len(fnameParts) == 3
        else:
            valid = valid and len(fnameParts) == 2
        #last part of filename is digit
        valid = valid and fnameParts[-1].isdigit()
        return valid


s = SystemDir("hps")
for k in s.entries.keys():
    print k, s.entries[k]

