def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""

	def __init__(self, x, y, srid=None):
		self.x = x
		self.y = y
		if srid is not None:
			self.srid = srid
		else:
			self.srid = srid_map.get(name)

	def to_wkt(self):
		return "POINT({0} {1})".format(self.x, self.y)

	def to_geojson(self):
		return {
			"type": "Point",
			"coordinates": [self.x, self.y]
		}

	Point = type(name, (object,), {
		"x": property(lambda self: self.x),
		"y": property(lambda self: self.y),
		"srid": property(lambda self: self.srid),
		"__init__": __init__,
		"to_wkt": to_wkt,
		"to_geojson": to_geojson
	})

	return Point