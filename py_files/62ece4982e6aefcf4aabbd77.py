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
	if frequency == 'always':
		return None

	freq = frequency.split()
	if len(freq) != 2:
		raise ValueError("Invalid frequency: %s" % frequency)
	try:
		number = int(freq[0])
	except ValueError:
		raise ValueError("Invalid frequency: %s" % frequency)
	unit = freq[1]
	if unit not in ['day', 'hour', 'minute', 'second']:
		raise ValueError("Invalid frequency: %s" % frequency)
	return timedelta(seconds=number * _TIME_UNITS[unit])