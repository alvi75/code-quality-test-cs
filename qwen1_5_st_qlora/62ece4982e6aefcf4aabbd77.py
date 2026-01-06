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

	pattern = re.compile(r'(\d+)(\w+)')

	m = pattern.match(frequency)
	if m:
		number = int(m.group(1))
		unit = m.group(2).lower()
	else:
		raise ValueError("Cannot parse frequency %s" % (frequency))

	if unit == 'day':
		days = number
	elif unit == 'week':
		days = 7 * number
	elif unit == 'month':
		days = 30 * number
	elif unit == 'year':
		days = 365 * number
	else:
		raise ValueError("Unknown unit %s for frequency %s" % (unit, frequency))

	return timedelta(days=days)