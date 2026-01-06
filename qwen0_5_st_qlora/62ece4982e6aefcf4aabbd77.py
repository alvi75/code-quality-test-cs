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

	freq = re.findall(r'\d+ (\w+)', frequency)
	if len(freq) != 2:
		raise ValueError("Invalid frequency: %s" % frequency)
	unit = freq[0]
	number = int(freq[1])
	if unit not in ['day', 'hour', 'minute', 'second']:
		raise ValueError("Invalid frequency: %s" % frequency)
	return datetime.timedelta(**{unit: number})