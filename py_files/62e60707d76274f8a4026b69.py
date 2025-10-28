def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	def __init__(self, *args, **kwargs):
		if len(args) == 1:
			self._x = args[0]
			self._y = None
		elif len(args) == 2:
			self._x = args[0]
			self._y = args[1]
		else:
			raise TypeError("Point constructor takes at most two arguments")
		for k in kwargs.keys():
			setattr(self, k, kwargs[k])
		self.srid = srid_map.get(kwargs.get('srid', 'EPSG:4326'), 'EPSG:4326')
		self.type = name

	def _get_x(self):
		return self._x
	def _set_x(self, value):
		self._x = value
	x = property(_get_x, _set_x)

	def _get_y(self):
		return self._y
	def _set_y(self, value):
		self._y = value
	y = property(_get_y, _set_y)

	def _get_srid(self):
		return self.srid
	def _set_srid(self, value):
		self.srid = value
	srid = property(_get_srid, _set_srid)

	def _get_type(self):
		return self.type
	type = property(_get_type)

	def __str__(self):
		return "POINT ({}, {})".format(self.x, self.y)
	
	def __repr__(self):
		return "Point({}, {}, {})".format(self.x, self.y, self.srid)

	def __eq__(self, other):
		if not isinstance(other, Point):
			return False
		return (self.x == other.x and self.y == other.y and self.srid == other.srid)

	def __ne__(self, other):
		return not self.__eq__(other)

	def __hash__(self):
		return hash((self.x, self.y, self.srid))

	def __lt__(self, other):
		if not isinstance(other, Point):
			return NotImplemented
		return (self.x < other.x or (self.x == other.x and self.y < other.y))

	def __le__(self, other):
		if not isinstance(other, Point):
			return NotImplemented
		return (self.x <= other.x or (self.x == other.x and self.y <= other.y))

	def __gt__(self, other