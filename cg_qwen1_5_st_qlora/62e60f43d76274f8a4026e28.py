def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(tz, datetime.tzinfo):
		tz = pytz.timezone(tz)
	return tz.fromutc(datetime.datetime.utcfromtimestamp(
		nanoseconds / 10**9))