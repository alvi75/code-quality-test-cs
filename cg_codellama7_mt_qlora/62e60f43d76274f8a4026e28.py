def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if tz is None:
		tz = pytz.UTC
	return tz.localize(datetime.datetime.utcfromtimestamp(nanoseconds / 1000000000.0))