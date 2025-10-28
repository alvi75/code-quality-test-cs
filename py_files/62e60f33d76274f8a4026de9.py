def dehydrate_point(value):
	"""
	The structure class is generated based on the value length.
	"""
	if len(value) == 1:
		return 'a'
	elif len(value) == 2:
		return 'ab'
	elif len(value) == 3:
		return 'abc'
	elif len(value) == 4:
		return 'abcd'
	elif len(value) == 5:
		return 'abcde'
	else:
		raise ValueError('Value too long')