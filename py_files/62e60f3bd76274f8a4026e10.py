def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	return [value.days, value.seconds, value.microseconds]