import os
from entry import Entry


##################################
# SystemDir
#
# holds information about a
# directory of files pertaining
# to a particular polynomial
# system
##################################
class SystemDir:
    def __init__(self, systemDir):
        self.systemDir = systemDir
        self.entries   = {}
        self.types     = {}

        # read filenames and layout data 
        for fname in os.listdir(systemDir):
            
            if not self.validName(fname):
                print "Invalid filename: ", fname
                continue

            filePath = systemDir + '/' + fname
            fnameParts = fname.split('.')
            entryType = fnameParts[0]
            entryNum = fnameParts[-1]

            if not self.entries.has_key (entryNum):                 # record info 
                self.entries[entryNum] = [Entry(filePath)]
            else:
                self.entries[entryNum].append (Entry(filePath))

            if not self.types.has_key (entryType):
                self.types[entryType] = set ([entryNum])
            else:
                self.types[entryType].add (entryNum)
            

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
for k in s.types.keys():
    print k, s.types[k]

