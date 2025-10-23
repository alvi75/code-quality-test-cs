def parse_frequency(frequency):
	"""
	Given a frequency string with a number and a unit of time, return a corresponding
     datetime.timedelta instance.
     If the frequency is None or "always", return None.
     Raise ValueError if the given frequency cannot be parsed.
     For instance, given "3 timeunit", return datetime.timedelta(timeunit=3)

     @param frequency :  A frequency string "number timeunit"

    @return str, the corresponding datetime
	"""
	if not frequency:
		return None

	frequency = frequency.strip()
	if frequency == 'always':
		return None

	try:
		number, timeunit = frequency.split(' ')
	except ValueError:
		raise ValueError("Frequency must be in the form of 'number timeunit'")

	try:
		number = int(number)
	except ValueError:
		raise ValueError("Number must be an integer")

	timeunit = timeunit.lower()

	if timeunit == 'second':
		return timedelta(seconds=number)
	elif timeunit == 'minute':
		return timedelta(minutes=number)
	elif timeunit == 'hour':
		return timedelta(hours=number)
	elif timeunit == 'day':
		return timedelta(days=number)
	elif timeunit == 'week':
		return timedelta(weeks=number)
	else:
		raise ValueError("Time unit must be one of second, minute, hour, day, week")