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

	freq = frequency.split()
	number, unit = freq[0], freq[1]
	if not number.isdigit():
		raise ValueError("Invalid number in frequency: %s" % (frequency))
	
	timescale = {
		"day": 24*60*60,
		"hour": 60*60,
		"minute": 60,
		"second": 1,
		"millisecond": 1e-3,
		"microsecond": 1e-6,
		"nanosecond": 1e-9,
	}
	
	for f in timescale.keys():
		if int(number) == 0:
			continue
		elif int(number) % float(timescale[f]) != 0:
			raise ValueError("%s can't divide to %d" % (f, number))
	
	if unit.lower() == "always":
		return None
	
	timeunit = timescale[unit.lower()]
	return datetime.timedelta(seconds=int(number)*timeunit)