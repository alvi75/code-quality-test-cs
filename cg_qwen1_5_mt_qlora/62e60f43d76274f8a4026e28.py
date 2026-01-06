def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, int) or nanoseconds < 0:
		raise ValueError("nanoseconds must be positive integer")
	return datetime.datetime.utcfromtimestamp(float(nanoseconds)/1e9).replace(tzinfo=pytz.UTC)