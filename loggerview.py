import gtk

class LoggerView (gtk.ScrolledWindow):

    def on_activate (self, path, col, param):
	if (self.active_iter != None):
	    self.store.set_value (self.active_iter, 0, 0)
	(model, self.active_iter) = self.view.get_selection().get_selected()
	self.store.set_value (self.active_iter, 0, 1)
	id   = self.store.get_value (self.active_iter, 1)
	name = self.store.get_value (self.active_iter, 2)
	self.activate_callback (id, name)

    def __init__ (self):
	gtk.ScrolledWindow.__init__ (self)
        self.set_shadow_type (gtk.SHADOW_IN)

	self.store = gtk.ListStore ('gboolean', int, str, str)
	self.view = gtk.TreeView (self.store)

	cell = gtk.CellRendererText()
	cell.set_property ('cell-background', 'yellow')

	col1 = gtk.TreeViewColumn ('Name')
	col2 = gtk.TreeViewColumn ('Description')

	col1.pack_start (cell, True)
	col2.pack_start (cell, True)

	col1.set_attributes(cell, text=2, cell_background_set = 0)
	col2.set_attributes(cell, text=3, cell_background_set = 0)

	self.view.append_column (col1)
	self.view.append_column (col2)

	self.view.connect ('row-activated', self.on_activate)
	self.set_policy (gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
	self.set_border_width (4)
	self.add (self.view)
	self.view.show()

	self.active_iter = None

    def append (self, i, shortname, longname):
        self.store.append ([0, i, shortname, longname])

    def clear (self):
        self.store.clear()
        self.active_iter = None
