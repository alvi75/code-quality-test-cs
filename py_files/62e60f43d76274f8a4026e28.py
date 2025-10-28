def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, int):
		raise TypeError("nanoseconds must be an integer")

	if nanoseconds < 0:
		raise ValueError("nanoseconds cannot be negative")

	if nanoseconds > 999999999999999999:
		raise ValueError("nanoseconds cannot be greater than 999999999999999999")

	return datetime.datetime.utcfromtimestamp(nanoseconds / 1000000000)