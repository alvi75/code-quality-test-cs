def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 2:
		return Point2D(value[0], value[1])
	elif len(value) == 3:
		return Point3D(value[0], value[1], value[2])
	else:
		raise ValueError("Invalid point length: %s" % len(value))