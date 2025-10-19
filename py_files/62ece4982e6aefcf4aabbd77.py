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

	freq = frequency.strip().lower()
	if freq == 'always':
		return None

	match = re.match(r'(\d+)\s*(\w+)', freq)
	if match:
		number, unit = int(match.group(1)), match.group(2).strip()
		try:
			return timedelta(**{unit: number})
		except Exception as e:
			raise ValueError("Invalid frequency '%s': %s" % (frequency, e))
	else:
		raise ValueError("Invalid frequency '%s'" % frequency)