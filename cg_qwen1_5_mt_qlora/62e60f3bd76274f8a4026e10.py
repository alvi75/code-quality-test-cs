def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, datetime.timedelta):
		return Struct(
			days=value.days,
			hours=value.seconds // 3600,
			minutes=(value.seconds % 3600) // 60,
			seconds=value.seconds % 60,
			microseconds=value.microseconds,
		)
	else:
		raise TypeError("Expected a datetime.timedelta")