class Path:
    soln = None
    logs = {} 

class SystemDir:
    SOLUTION_TYPES = ["soln", "failed","div"]

    paths = {}
    def __init__(self, systemDir):
        self.systemDir = systemDir

        # read filenames and layout data 
        for fname in os.listdir(systemDir):
            filePath = systemDir + '/' + fname
            fnameParts = fname.split('.')
            pathNum = fParts[-1]
            
            if fnameParts[0].startswith("log"): # log file
                logType = fParts[1]
                if self.paths[pathNum] == None: # path not initialized
                    self.paths[pathNum] = Path()
                self.paths[pathNum].logs[logtype] = Log(filepath)   

            else:
                if self.paths[pathNum] == None:
                    self.paths[pathNum].soln = Path()
                self.paths[pathNum].soln = Soln(filepath)

