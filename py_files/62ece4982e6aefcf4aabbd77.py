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
	if not isinstance(frequency, basestring):
		raise TypeError("frequency must be a string")
	frequency = frequency.strip()
	if frequency == 'always':
		return None

	try:
		number, unit = frequency.split(' ', 1)
	except ValueError:
		raise ValueError("Invalid frequency: %s" % frequency)

	unit = unit.lower()

	if unit in ('', 'none'):
		return None

	if unit not in ('day', 'hour', 'minute', 'second', 'microsecond', 'millisecond',
					'millisecond', 'microsecond', 'second', 'minute', 'hour', 'day'):
		raise ValueError("Invalid frequency: %s" % frequency)

	if unit == 'day':
		return datetime.timedelta(days=int(number))
	elif unit == 'hour':
		return datetime.timedelta(hours=int(number))
	elif unit == 'minute':
		return datetime.timedelta(minutes=int(number))
	elif unit == 'second':
		return datetime.timedelta(seconds=int(number))
	elif unit == 'microsecond':
		return datetime.timedelta(microseconds=int(number) * 1000000)
	elif unit == 'millisecond':
		return datetime.timedelta(milliseconds=int(number) * 1000)
	else:
		return datetime.timedelta(seconds=float(number))