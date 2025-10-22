def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 2:
		return (value[0], value[1])
	elif len(value) == 3:
		return (value[0], value[1], value[2])
	else:
		raise ValueError("Invalid point value")