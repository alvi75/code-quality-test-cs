def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class Point(object):
		def __init__(self, *args, **kwargs):
			for field in fields:
				if field in kwargs:
					setattr(self, field, kwargs[field])
				else:
					setattr(self, field, None)
			self.srid = srid_map.get(self.wkb_type, 4326)

		def __repr__(self):
			return '<%s %s>' % (name, self.__dict__)

		def __eq__(self, other):
			return self.__dict__ == other.__dict__

		def __ne__(self, other):
			return not self.__eq__(other)

		def __hash__(self):
			return hash(tuple(sorted(self.__dict__.items())))

		def __getattr__(self, name):
			raise AttributeError("'%s' has no attribute '%s'" % (name, name))

		def __setattr__(self, name, value):
			raise AttributeError("'%s' has no attribute '%s'" % (name, name))

		def __getstate__(self):
			return self.__dict__

		def __setstate__(self, state):
			self.__dict__ = state

		def __copy__(self):
			return type(self)(**self.__dict__)

		def __deepcopy__(self, memo={}):
			return type(self)(**self.__dict__)

		def as_wkt(self):
			return wkt.dumps(self)

		def as_wkb(self):
			return wkb.dumps(self)

		def as_geojson(self):
			return geojson.dumps(self)

		def as_dict(self):
			return dict(self.__dict__)

		def as_tuple(self):
			return tuple(self.__dict__.values())

		def as_list(self):
			return list(self.__dict__.values())

		def as_namedtuple(self):
			return collections.namedtuple('Point', self.__dict__.keys())(**self.__dict__)

		def as_record(self):
			return Record(**self.__dict__)

		def as_row(self):
			return Row(**self.__dict__)

		def as_row_with_srid(self):
			return RowWithSRID(**self.__dict__)

		def as_row_with_srid_and_geom(self):
			return RowWithSRIDAndGeom(**self.__dict__)

		def as_row_with_geom(self):
			return RowWithGeom(**self.__dict__)

		def as_row_with_geom_and_srid(self