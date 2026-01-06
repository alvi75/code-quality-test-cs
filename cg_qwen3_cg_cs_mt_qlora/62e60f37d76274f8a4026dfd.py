def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, datetime.datetime):
		return value.strftime('%Y-%m-%dT%H:%M:%S')
	else:
		return value