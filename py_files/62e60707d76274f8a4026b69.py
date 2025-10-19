def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class_name = name

	def __init__(self, *args, **kwargs):
		if len(args) == 1:
			if type(args[0]) in (list, tuple):
				self.x, self.y = args[0]
			else:
				self.x = self.y = args[0]
		elif len(args) == 2:
			self.x, self.y = args
		elif 'x' in kwargs and 'y' in kwargs:
			self.x, self.y = kwargs['x'], kwargs['y']
		else:
			raise TypeError("Point takes exactly two arguments")

	def to_wkt(self):
		return "POINT({0} {1})".format(self.x, self.y)

	def to_json(self):
		return json.dumps({
			"type": "Point",
			"coordinates": [self.x, self.y]
		})

	def to_dict(self):
		return dict(x=self.x, y=self.y)

	def __repr__(self):
		return "{0}({1}, {2})".format(class_name, self.x, self.y)

	def __str__(self):
		return "{0}({1}, {2})".format(class_name, self.x, self.y)

	new_class = type(class_name, (object,), {
		__init__: __init__,
		to_wkt: to_wkt,
		to_json: to_json,
		to_dict: to_dict,
		__repr__: __repr__,
		__str__: __str__
	})
	return new_class