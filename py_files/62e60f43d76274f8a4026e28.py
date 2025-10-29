def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, int):
		raise TypeError("nanoseconds must be an integer")

	if tz is None:
		tz = timezone.utc

	return datetime.datetime.fromtimestamp(
		nanoseconds / 1000000000,
		tz=tz)