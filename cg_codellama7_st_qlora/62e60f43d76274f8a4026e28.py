def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if nanoseconds is None:
		return None
	if tz is None:
		return time.strftime("%H:%M:%S", time.gmtime(nanoseconds / 1000000000))
	else:
		return time.strftime("%H:%M:%S", time.localtime(nanoseconds / 1000000000))