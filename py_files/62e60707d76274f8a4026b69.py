def point_type(name, fields, srid_map):
		"""
		Dynamically Generating Point Class
		"""
		class _Point(object):
			__slots__ = [f[0] for f in fields]
			srid = srid_map[name]

			def __init__(self, *args, **kwargs):
				for i, arg in enumerate(args):
					self.__slots__[i] = arg

			def __repr__(self):
				return "({})".format(", ".join([str(getattr(self, f)) for f in self.__slots__]))

		return _Point

	return point_type