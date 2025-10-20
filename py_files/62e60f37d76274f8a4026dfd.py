def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, time.Time):
		return value.ticks
	elif isinstance(value, int) or isinstance(value, float):
		return value
	else:
		raise TypeError("Value must be a Time object or integer")