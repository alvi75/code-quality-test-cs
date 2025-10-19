def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 0:
		return None

	if len(value) == 1:
		return Point(value[0])

	elif len(value) == 2:
		return Point(int(value[0]), int(value[1]))

	else:
		raise ValueError("Invalid point: %s" % repr(value))