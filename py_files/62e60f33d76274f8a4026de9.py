def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 2:
		return Point(value[0], value[1])
	elif len(value) == 3:
		return Point(value[0], value[1], value[2])