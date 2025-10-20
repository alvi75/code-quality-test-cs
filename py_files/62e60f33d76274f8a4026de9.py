def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return 'char'
	elif len(value) == 2:
		return 'short'
	elif len(value) == 4:
		return 'int'
	elif len(value) == 8:
		return 'long'
	else:
		raise ValueError('Invalid point length: %s' % len(value))