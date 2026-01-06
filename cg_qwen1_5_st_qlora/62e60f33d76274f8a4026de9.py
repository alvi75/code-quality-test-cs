def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return struct.pack('>B', value[0])
	elif len(value) == 2:
		return struct.pack('>H', value[0] << 8 | value[1])
	else:
		raise ValueError("Point must be of length 1 or 2")