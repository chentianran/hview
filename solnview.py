import gtk

class SolnView (gtk.ScrolledWindow):
    def on_activate (self, path, col, param):
	if (self.active_iter != None):
	    self.store.set_value (self.active_iter, 0, 0)
	(model, self.active_iter) = self.view.get_selection().get_selected()
	self.store.set_value (self.active_iter, 0, 1)
	self.active_id = self.store.get_value (self.active_iter, 1)
	self.activate_callback (self.active_id)

    def __init__ (self):
	gtk.ScrolledWindow.__init__ (self)
        
        self.set_shadow_type (gtk.SHADOW_IN)

	self.store = gtk.ListStore ('gboolean', int, 'gdouble', 'gdouble', 'gdouble', 'gdouble')
	self.names = ['Id', 'Norm', 'Cond.', 'Tangent', 'T']
	self.view = gtk.TreeView (self.store)
	#self.view.set_headers_clickable (True)

	self.cell = gtk.CellRendererText()
	self.cell.set_property ('cell-background', 'yellow')

	self.cols = map (lambda x: gtk.TreeViewColumn (x), self.names)
	for i in range (len (self.cols)):
	    c = self.cols[i]
	    self.view.append_column (c)
	    c.pack_start (self.cell, True)
	    c.set_attributes(self.cell, text=(i+1), cell_background_set = 0)
	    c.set_sort_indicator (True)
	    c.set_sort_column_id (i+1)

	self.view.connect ('row-activated', self.on_activate)

	self.active_iter = None

	self.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
	self.set_border_width (4)
	self.add (self.view)
	self.view.show()

    def append (self, s):
        i    = int  (s['id'])
	norm = float(s['norm'])
	cond = float(s['condition'])
	dx   = float(s['max_dx'])
	t    = float(s['t'])
	self.store.append ([0, i, norm, cond, dx, t])


