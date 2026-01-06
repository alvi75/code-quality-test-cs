def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, datetime.datetime):
		return value.strftime('%Y-%m-%dT%H:%M:%S.%f')
	elif isinstance(value, datetime.date):
		return value.strftime('%Y-%m-%d')
	else:
		raise ValueError("Unknown type for time: %s" % type(value))