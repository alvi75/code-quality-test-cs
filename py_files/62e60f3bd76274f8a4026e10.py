def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, timedelta):
		return timedelta_to_struct(value)
	else:
		raise TypeError("value must be a timedelta")