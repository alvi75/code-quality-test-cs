def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 2:
		return (value[0], value[1])
	elif len(value) == 4:
		return ((value[0], value[1]), (value[2], value[3]))
	else:
		raise ValueError("Invalid point length: %s" % len(value))