def dehydrate_time(value):
	"""
	Use ticks in the Time class to generate the Structure class.
	"""
	if isinstance(value, Time):
		return {
			"ticks": value.ticks,
			"seconds": value.seconds,
			"nanoseconds": value.nanoseconds
		}
	else:
		raise TypeError("dehydrated time must be a Time instance")