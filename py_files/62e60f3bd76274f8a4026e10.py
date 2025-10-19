def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, timedelta):
		return TimedeltaStructure(value)
	elif isinstance(value, (int, float)):
		return FixedLengthStructure(str(value))
	else:
		raise TypeError("Can only dehydrate timedelta or int/float")