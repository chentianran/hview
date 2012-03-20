import gtk

from matplotlib.figure import Figure
from numpy import arange, sin, pi
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas
from matplotlib.backends.backend_gtkagg import NavigationToolbar2GTKAgg as NavigationToolbar

#class LoggerPlot (FigureCanvas):
class LoggerPlot (gtk.VBox):

    def __init__ (self):
        gtk.VBox.__init__ (self)
        self.figure  = Figure(figsize=(5,4), dpi=100)
        self.canvas  = FigureCanvas (self.figure)
        self.toolbar = NavigationToolbar (self.canvas, None)

        self.pack_start (self.canvas)
        self.pack_start (self.toolbar, False, False)

        #FigureCanvas.__init__ (self, self.figure)

    def plot (self, title, x, y):
        self.figure.clear()
        a = self.figure.add_subplot(111)
        a.set_title (title)
        a.grid(True)
        a.plot(x,y)
        self.canvas.draw()

    def clear (self):
        self.figure.clear()
        self.canvas.draw()
