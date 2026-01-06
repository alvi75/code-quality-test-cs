def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, datetime.datetime):
		return Time(value)
	elif isinstance(value, datetime.date):
		return Date(value)
	else:
		raise TypeError("Can't dehydrate %s" % type(value))