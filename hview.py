#!/usr/bin/env python

import gtk
import sys

from solnview   import *
from solnload   import *
from loggerview import *
from loggerplot import *
from loggerload import *
from getopt     import *

class MainFrame (gtk.Window):

    pages = []

    def __init__ (self, path, width, height):
        gtk.Window.__init__ (self)

        solnview = SolnView()
        failview = SolnView()

        SolnLoad (path, 'soln',   solnview)
        SolnLoad (path, 'failed', failview)

        self.loggerview = LoggerView()
        self.loggerplot = LoggerPlot()
        self.loggerload = LoggerLoad (path, self.loggerview, self.loggerplot)

        solnview.activate_callback = self.loggerload.soln_on_activate
        failview.activate_callback = self.loggerload.soln_on_activate

        self.loggerplot.set_size_request (width/2, height/2)

        notebook = gtk.Notebook()
        #notebook.append_page (self.all_box, gtk.Label ('Summary'))
        notebook.append_page (solnview, gtk.Label ('Solutions'))
        notebook.append_page (failview, gtk.Label ('Failed Paths'))

        hbox = gtk.HBox (False, 3)
        hbox.pack_start (self.loggerview, True, True)
        hbox.pack_start (self.loggerplot, True, True)

        vpane = gtk.VPaned()
        vpane.pack1 (notebook, True, True)
        vpane.pack2 (hbox, False, True)


        self.add (vpane)
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
