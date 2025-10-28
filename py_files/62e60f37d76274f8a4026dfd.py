def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if value is None:
		return None

	t = Time(value)
	return Structure(t)