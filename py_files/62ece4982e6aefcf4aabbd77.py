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
		raise ValueError("Invalid frequency: %s" % frequency)

	if not number.isdigit():
		raise ValueError("Invalid frequency: %s" % frequency)

	timeunit = timeunit.lower()

	if timeunit in ['day', 'days']:
		return timedelta(days=int(number))
	elif timeunit in ['hour', 'hours']:
		return timedelta(hours=int(number))
	elif timeunit in ['minute', 'minutes']:
		return timedelta(minutes=int(number))
	elif timeunit in ['second', 'seconds']:
		return timedelta(seconds=int(number))
	else:
		raise ValueError("Invalid frequency: %s" % frequency)