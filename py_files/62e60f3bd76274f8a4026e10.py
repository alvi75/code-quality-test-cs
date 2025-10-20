def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, timedelta):
		return value.days, value.seconds, value.microseconds
	else:
		raise ValueError("Timedelta must be a datetime.timedelta object")