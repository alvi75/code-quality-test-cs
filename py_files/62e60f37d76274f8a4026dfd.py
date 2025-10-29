def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, (int, float)):
		return Time(ticks=value)
	elif isinstance(value, datetime.datetime):
		return Time(ticks=int(time.mktime(value.timetuple()) * 1000 + value.microsecond / 1000))
	else:
		raise TypeError("Can't dehydrate %s" % type(value))