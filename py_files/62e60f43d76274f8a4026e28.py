def hydrate_time(nanoseconds, tz=None):
	"""
	Convert nanoseconds to a time in fixed format.
	"""
	if not isinstance(nanoseconds, int):
		raise TypeError("nanoseconds must be an integer")
	if nanoseconds < 0:
		raise ValueError("nanoseconds must be greater than or equal to zero")

	# convert to seconds
	seconds = nanoseconds / 1e9

	# convert to microseconds
	micros = nanoseconds % 1e9

	# convert to milliseconds
	millis = micros / 1e6

	# convert to hours
	hours = millis / 1e3

	# convert to minutes
	minutes = hours / 60

	# convert to days
	days = minutes / 60

	# convert to years
	years = days / 365

	# convert to timezone aware datetime
	tzaware_datetime = datetime.datetime.utcfromtimestamp(days)

	# convert to timezone aware datetime with timezone
	tzaware_datetime_with_timezone = tzaware_datetime.replace(tzinfo=tz)

	return tzaware_datetime_with_timezone