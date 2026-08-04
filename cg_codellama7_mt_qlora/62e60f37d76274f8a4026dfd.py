def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if value is None:
		return None
	return Time(value.hour, value.minute, value.second, value.microsecond)