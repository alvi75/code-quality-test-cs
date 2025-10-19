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

	freq = re.match(r'(\d+)([a-zA-Z]+)', frequency)
	if not freq:
		raise ValueError("Invalid frequency: %s" % (frequency,))

	number = int(freq.group(1))
	unit = freq.group(2).lower()

	if unit == 'day':
		return timedelta(days=number)
	elif unit == 'hour':
		return timedelta(hours=number)
	elif unit == 'minute':
		return timedelta(minutes=number)
	elif unit == 'second':
		return timedelta(seconds=number)
	else:
		raise ValueError("Unknown unit: %s" % (unit,))