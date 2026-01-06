def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""

	def __init__(self, *args, **kwargs):
		if len(args) == 1:
			args = args[0]
		if isinstance(args, dict):
			self._data = args
		else:
			self._data = {}
			for field in fields:
				value = kwargs.get(field)
				if value is not None:
					self._data[field] = value

	def to_dict(self):
		return self._data

	def to_wkt(self):
		wkt = "POINT"
		for field in fields:
			wkt += " %s" % self._data[field]
		return wkt

	def to_srid(self, srid):
		srid = int(srid)
		if srid in srid_map:
			return srid_map[srid]
		else:
			raise ValueError("Invalid SRID: %d" % srid)

	def __repr__(self):
		return "<%s(%s)>" % (name, self.to_wkt())

	return type(name, (object,), {
		__init__: __init__,
		to_dict: to_dict,
		to_wkt: to_wkt,
		to_srid: to_srid,
		__repr__: __repr__
	})