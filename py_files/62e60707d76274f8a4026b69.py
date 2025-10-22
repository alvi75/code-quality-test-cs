def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""

	class Point(geo.Point):
		def __init__(self, *args, **kwargs):
			super(Point, self).__init__(*args, **kwargs)
			self.srid = srid_map.get(self.__class__.__name__, 4326)

	return Point