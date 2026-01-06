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

	try:
		number = int(re.match(r'(\d+)', frequency).group(1))
	except ValueError as e:
		raise ValueError("Invalid frequency: %s" % frequency)
	unit = re.sub(r'\D', '', frequency)
	if unit == 'day':
		timeunit = timedelta(days=number)
	elif unit == 'hour':
		timeunit = timedelta(hours=number)
	elif unit == 'minute':
		timeunit = timedelta(minutes=number)
	else:
		raise ValueError("Unknown unit in frequency: %s" % frequency)

	return timeunit