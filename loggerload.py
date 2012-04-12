import sys
import glob
import re

#current state:
#

class LoggerLoad:

    def logger_on_activate (self, i, name):
        path = self.prefix + 'log.' + name + '.' + str(i)
        title = name
        f = open (path, 'r')
        x = []
        y = []
        begin = False
        for line in f:
            if (begin):
                if (re.match("^END",line)):
                    break
                l = line.split()
                x.append(float(l[0]))
                y.append(float(l[1]))
            elif (re.match("^BEGIN",line)):
                begin = True;
            else:
                m_title = re.match ('^title:\s*(.+)$', line)
                if (m_title):
                    title = m_title.group(1)
        f.close()
        self.plot.plot (title, x, y)

    def soln_on_activate (self, i):
        self.view.clear()
        self.plot.clear()
        ex = 'log\.([^\.]+).' + str(i) + '$'
        for entry in glob.glob (self.prefix + 'log.*'):
            m = re.search (ex, entry)
            if m:
                shortname = m.group(1)
                longname  = '...'
                f = open (entry, 'r')
                for line in f:
                    m_long = re.match ('^longname:\s*(.+)$', line)
                    if (m_long):
                        longname = m_long.group(1)
                        break
                    elif (re.match("^BEGIN",line)):
                        break
                self.view.append (i, shortname, longname)

    def __init__ (self, prefix, view, plot):
        self.prefix = prefix
        self.view = view
        self.view.activate_callback = self.logger_on_activate
        self.plot = plot

