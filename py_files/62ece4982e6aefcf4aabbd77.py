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

	parts = frequency.split()
	if len(parts) != 2:
		raise ValueError("Invalid frequency: %s" % frequency)
	number = int(parts[0])
	unit = parts[1]
	try:
		datetime_unit = getattr(datetime.timedelta, unit.lower())
	except AttributeError:
		raise ValueError("Unknown unit in frequency: %s" % frequency)
	return datetime.timedelta(**{unit.lower(): number})