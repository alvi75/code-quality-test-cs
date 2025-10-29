def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	def __init__(self, *args, **kwargs):
		self.__dict__.update(kwargs)
		if 'geometry' in self.__dict__:
			raise ValueError("Point already initialized")
		self.__dict__.update({'geometry': geometry.Point(*args, **kwargs)})
		return self

	def __repr__(self):
		return "<%s: %s>" % (name, str(self.geometry))

	def __str__(self):
		return str(self.geometry)

	def __hash__(self):
		return hash((self.__class__.__name__, tuple(sorted(self.__dict__.items()))))

	def __eq__(self, other):
		if not isinstance(other, Point):
			return False
		return self.__dict__ == other.__dict__

	def __lt__(self, other):
		if not isinstance(other, Point):
			return False
		return self.__dict__ < other.__dict__

	def __gt__(self, other):
		if not isinstance(other, Point):
			return False
		return self.__dict__ > other.__dict__

	def __le__(self, other):
		if not isinstance(other, Point):
			return False
		return self.__dict__ <= other.__dict__

	def __ge__(self, other):
		if not isinstance(other, Point):
			return False
		return self.__dict__ >= other.__dict__

	def __getitem__(self, key):
		if key in ['x', 'y']:
			return self.geometry[key]
		elif key in ['z', 'm']:
			return self.geometry[key] / 1000000
		else:
			return self.geometry[key]

	def __setitem__(self, key, value):
		if key in ['x', 'y']:
			self.geometry[key] = value
		elif key in ['z', 'm']:
			self.geometry[key] = value / 1000000
		else:
			raise AttributeError('Invalid attribute name')

	def __delitem__(self, key):
		if key in ['x', 'y']:
			del self.geometry[key]
		elif key in ['z', 'm']:
			del self.geometry[key] / 1000000
		else:
			raise AttributeError('Invalid attribute name')

	def __iter__(self):
		for field in self.geometry.fields:
			yield field

	def __len__(self):
		return len