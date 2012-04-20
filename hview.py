#!/usr/bin/env python

import gtk
import sys

from solnview   import *
from solnload   import *
from loggerview import *
from loggerplot import *
from loggerload import *
from getopt     import *

from page import *

class MainFrame (gtk.Window):

    pages = []

    def __init__ (self, path, width, height):
        gtk.Window.__init__ (self)

        self.path = path
        self.width = width
        self.height = height
        
        solnview = Page(self)
        failview = Page(self)

        notebook = gtk.Notebook()
        #notebook.append_page (self.all_box, gtk.Label ('Summary'))
        notebook.append_page (solnview, gtk.Label ('Solutions'))
        notebook.append_page (failview, gtk.Label ('Failed Paths'))

        self.add (notebook)
        self.set_default_size (width, height)

width    = 800
height   = 600
options  = "w:h:"
optlist, args = getopt(sys.argv[1:], options)

if len(args) == 0:
    print "Usage: hview PATH_TO_HOM4PS_FILES [-w WIDTH] [-h HEIGHT]"

path     = args[0]

for op, arg in optlist:
     if op   == "-w":
        width  = int(arg)
     elif op == "-h":
        height = int(arg)

frame = MainFrame(path, width, height)
frame.connect ("delete_event", gtk.main_quit)
frame.set_title ('HOM4PS3 Viewer')
frame.show_all()

gtk.main()
