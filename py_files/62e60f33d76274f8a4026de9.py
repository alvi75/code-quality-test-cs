def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return struct.pack('B', value[0])
	elif len(value) == 2:
		return struct.pack('>H', value)
	else:
		raise ValueError("Point must be a single byte or two bytes")