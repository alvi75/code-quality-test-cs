def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not nanoseconds:
		return None

	tz = tz or pytz.utc
	return datetime.datetime.fromtimestamp(
		nanoseconds / 1000000000,
		tz=tz).time()