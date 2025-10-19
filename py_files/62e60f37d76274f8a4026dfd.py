def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, time.struct_time):
		return value
	elif isinstance(value, datetime.datetime):
		value = value.timetuple()
		return (value[0], value[1], value[2], value[3], value[4], value[5],
				value[6], value[7], -1)
	else:
		raise TypeError("Cannot dehydrate %s" % type(value))