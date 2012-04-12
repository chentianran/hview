import sys
import glob
import re

#loads the solutions of a system of equations
#solutions are complex numbers

class SolnLoad:
    def __init__ (self, prefix, name, view):
        pattern = prefix + name + '.*'
        solns = glob.glob (pattern)
        for s in solns:
            m = re.search('\.([0-9]+)$',s)
            if m:
                dict = {}
                id = m.group(1)
                f = open(s,'r')
                for line in f:
                    rec = re.search('^([^\(:]+):\s*([0-9\.\-\+eE]+)', line)
                    if rec:
                        dict[rec.group(1)] = rec.group(2)
                view.addSoln(dict)

