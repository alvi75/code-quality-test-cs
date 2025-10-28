def point_type(name, fields, srid_map):
	"""
	Dynamically Generating Point Class
	"""
	if name in POINT_TYPES:
		return POINT_TYPES[name]
	point_type = type(name, (Point, ), dict(
		fields=fields,
		srid_map=srid_map,
	))
	POINT_TYPES[name] = point_type
	return point_type