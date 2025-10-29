def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return Point(value[0])
	elif len(value) == 2:
		return Point(float(value[0]), float(value[1]))
	else:
		raise ValueError("Invalid point: %s" % value)