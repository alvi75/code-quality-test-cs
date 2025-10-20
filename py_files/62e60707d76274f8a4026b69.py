def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	if name not in POINT_TYPES:
		raise Exception("Point type %s is not supported" % name)
	return POINT_TYPES[name](fields, srid_map)