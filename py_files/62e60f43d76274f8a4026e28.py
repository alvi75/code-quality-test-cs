def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	timestamp = datetime.datetime.utcfromtimestamp(nanoseconds / 1000000000)
	if tz is not None:
		timestamp = timestamp.replace(tzinfo=tz)

	return timestamp.strftime("%H:%M:%S.%f")[:-3]