def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, int) or nanoseconds < 0:
		raise ValueError("nanoseconds must be a non-negative integer")
	return datetime.datetime.utcfromtimestamp(nanoseconds / 1e9).replace(tzinfo=pytz.utc)