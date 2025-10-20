def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 2:
		return struct.pack('!h', value[0]), struct.pack('!h', value[1])
	elif len(value) == 3:
		return struct.pack('!h', value[0]), struct.pack('!h', value[1]), struct.pack('!h', value[2])