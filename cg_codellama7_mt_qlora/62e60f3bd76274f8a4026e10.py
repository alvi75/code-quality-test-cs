def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if value is None:
		return None
	return Structure(
		value.days,
		value.seconds,
		value.microseconds
	)