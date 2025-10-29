def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	class Point(geom_types.Point):
		__name__ = name

		def __init__(self, *args, **kwargs):
			if len(args) == 1:
				args = args[0]
			if isinstance(args, dict):
				args = args['coordinates']
			super(Point, self).__init__(*args, **kwargs)

		@classmethod
		def from_wkt(cls, wkt):
			return cls.from_wkb(wkt_to_wkb(wkt))

		@classmethod
		def from_wkb(cls, wkb):
			wkb = wkb_to_wkb(wkb)
			srid = wkb[7:15]
			if srid in srid_map:
				srid = srid_map[srid]
			else:
				srid = None
			return super(Point, cls).from_wkb(wkb, srid=srid)

		@classmethod
		def from_geojson(cls, geojson):
			return cls.from_wkb(wkb.loads(geojson['coordinates']))

		@classmethod
		def from_dict(cls, d):
			return cls(d['coordinates'])

		@classmethod
		def from_point(cls, p):
			return cls(p.x, p.y)

		@classmethod
		def from_point3d(cls, p):
			return cls(p.x, p.y, p.z)

		@classmethod
		def from_point4d(cls, p):
			return cls(p.x, p.y, p.z, p.w)

		@classmethod
		def from_xy(cls, x, y):
			return cls(x, y)

		@classmethod
		def from_xyz(cls, x, y, z):
			return cls(x, y, z)

		@classmethod
		def from_xym(cls, x, y, m):
			return cls(x, y, m)

		@classmethod
		def from_xyza(cls, x, y, z, a):
			return cls(x, y, z, a)

		@classmethod
		def from_xyzaa(cls, x, y, z, a, b):
			return cls(x, y, z, a, b)

		@classmethod
		def from_xyzaab(cls, x, y, z, a, b, c):
			return cls(x, y, z,