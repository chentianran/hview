import gtk
import sys

from solnview   import *
from solnload   import *
from loggerview import *
from loggerplot import *
from loggerload import *
from getopt     import *


class Page(gtk.Frame):
    def on_activate (self, path, col, param):
        if (self.active_iter != None):
            self.store.set_value (self.active_iter, 0, 0)
        (model, self.active_iter) = self.view.get_selection().get_selected()
        self.store.set_value (self.active_iter, 0, 1)
        self.active_id = self.store.get_value (self.active_iter, 1)
        self.activate_callback (self.active_id)

    def __init__ (self, parent):
        gtk.Frame.__init__(self)
        

        path = parent.path
        
        #page elements
        self.loggerview = LoggerView()
        self.loggerplot = LoggerPlot()
        self.loggerload = LoggerLoad (path, self.loggerview, self.loggerplot)
        self.solnview = SolnView()

        self.loggerplot.set_size_request (parent.width/2, parent.height/2)

  #      solnview.activate_callback = self.loggerload.soln_on_activate


        hbox = gtk.HBox (False, 3)
        hbox.pack_start (self.loggerview, True, True)
        hbox.pack_start (self.loggerplot, True, True)

        vpane = gtk.VPaned()

        vpane.pack1 (self.solnview, True, True)
        vpane.pack2 (hbox, False, True)

        self.view = vpane
 
        self.add (self.view)
        self.view.show()

