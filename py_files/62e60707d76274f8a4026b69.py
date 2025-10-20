def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	def __init__(self, *args, **kwargs):
		super(Point, self).__init__(*args, **kwargs)
		self._fields = fields

		if len(args) == 1:
			point = args[0]
			for field in self._fields:
				setattr(self, field, getattr(point, field))
		elif len(args) > 1:
			raise TypeError("Point constructor takes one argument")

	@property
	def x(self):
		return getattr(self, self._fields[0])

	@property
	def y(self):
		return getattr(self, self._fields[1])

	@property
	def z(self):
		return getattr(self, self._fields[2]) if len(self._fields) >= 3 else None

	@property
	def wkt(self):
		return "POINT ({})".format(", ".join([str(getattr(self, f)) for f in self._fields]))

	@property
	def wkb(self):
		wkb = WKBWriter()
		return wkb.write_point(self)

	@classmethod
	def from_wkt(cls, wkt):
		parts = wkt.split(' ')
		assert parts[0] == 'POINT'
		fields = [f.strip() for f in parts[1].split(',')]
		values = []
		for field in cls._fields:
			try:
				index = fields.index(field)
				value = float(fields[index])
			except ValueError:
				value = None
			values.append(value)
		return cls(*values)

	@classmethod
	def from_wkb(cls, wkb):
		return cls.from_wkt(WKTReader().read(wkb))

	@classmethod
	def from_json(cls, json):
		return cls.from_wkt(json['wkt'])

	@classmethod
	def from_dict(cls, d):
		return cls.from_wkt(d['wkt'])