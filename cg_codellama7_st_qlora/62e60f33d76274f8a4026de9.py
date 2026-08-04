def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if value is None:
		return None
	if isinstance(value, Point):
		return value
	if isinstance(value, tuple):
		return Point(*value)
	if isinstance(value, list):
		return Point(*value)
	if isinstance(value, dict):
		return Point(value['x'], value['y'])
	raise TypeError("Cannot dehydrate a point from %s" % type(value))