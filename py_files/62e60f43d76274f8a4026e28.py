def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, (int, long)):
		raise ValueError("nanoseconds must be int or long")
	if tz is None:
		tz = pytz.utc
	return datetime.datetime.fromtimestamp(nanoseconds / 1000000000.0, tz=tz).time()