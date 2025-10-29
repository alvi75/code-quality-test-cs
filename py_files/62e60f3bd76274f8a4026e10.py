def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, timedelta):
		return timedelta_to_struct(value)
	elif isinstance(value, datetime.timedelta):
		return timedelta_to_struct(value)
	else:
		raise TypeError("Can't dehydrate %s" % type(value))