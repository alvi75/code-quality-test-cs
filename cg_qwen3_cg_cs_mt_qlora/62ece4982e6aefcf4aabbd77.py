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

	frequency = frequency.lower()
	if frequency == 'always':
		return None

	try:
		number, unit = frequency.split(' ')
	except ValueError:
		raise ValueError("Invalid frequency: %s" % frequency)

	if unit not in ['day', 'days', 'hour', 'hours', 'minute', 'minutes']:
		raise ValueError("Invalid frequency: %s" % frequency)

	if number.isdigit():
		number = int(number)
	else:
		raise ValueError("Invalid frequency: %s" % frequency)

	if unit == 'day' or unit == 'days':
		return timedelta(days=number)
	elif unit == 'hour' or unit == 'hours':
		return timedelta(hours=number)
	elif unit == 'minute' or unit == 'minutes':
		return timedelta(minutes=number)