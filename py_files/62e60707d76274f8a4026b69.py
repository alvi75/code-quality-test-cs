def point_type(name, fields, srid_map):
		"""
		Dynamically Generating Point Class
		"""
		class Point(object):
			pass

		for field in fields:
			if field not in ['x', 'y']:
				raise ValueError('Field name must be x or y')

		def __init__(self, *args, **kwargs):
			self.__dict__['Point'] = super(Point, self).__class__
			self.__dict__[field] = kwargs.pop(field)
			self.__dict__['__srid_map__'] = srid_map
			self.__dict__['__fields__'] = fields
			super(Point, self).__init__(*args, **kwargs)

		def __repr__(self):
			return "Point(%s)" % (','.join([str(getattr(self, f)) for f in fields]))

		def __eq__(self, other):
			return all([getattr(self, f) == getattr(other, f) for f in fields])

		def __lt__(self, other):
			return bool(super(Point, self).__lt__(other))

		def __le__(self, other):
			return bool(super(Point, self).__le__(other))

		def __gt__(self, other):
			return bool(super(Point, self).__gt__(other))

		def __ge__(self, other):
			return bool(super(Point, self).__ge__(other))

		def __getitem__(self, key):
			return super(Point, self).__getitem__(key)

		def __delitem__(self, key):
			return super(Point, self).__delitem__(key)

		def __iter__(self):
			return iter(super(Point, self).__iter__())

		def __len__(self):
			return super(Point, self).__len__()

		def __nonzero__(self):
			return bool(super(Point, self).__nonzero__())

		def __float__(self):
			return float(super(Point, self).__float__())

		def __int__(self):
			return int(super(Point, self).__int__())

		def __bool__(self):
			return bool(super(Point, self).__bool__)

		def __enter__(self):
			return self

		def __exit__(self, type, value, traceback):
			return self

		Point.__name__ = name
		return Point

	# Return a class with same attributes as Point
	return point_type(name, fields, srid_map)