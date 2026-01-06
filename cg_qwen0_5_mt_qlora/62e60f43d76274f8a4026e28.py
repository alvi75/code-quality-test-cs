def hydrate_time(nanoseconds, tz=None):
	"""
	Hydrate time from nanoseconds.
	"""
	if not isinstance(nanoseconds, int):
		raise TypeError('nanoseconds must be an integer')
	if nanoseconds < 0:
		raise ValueError('nanoseconds cannot be negative')

	if tz is None:
		tz = timezone.utc

	return datetime.datetime.fromtimestamp(
		nanoseconds / 1e9,
		tz=tz
	)