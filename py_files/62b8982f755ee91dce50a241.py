def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	return Time(
		self.days,
		self.hours,
		self.minutes,
		self.seconds,
		self.microseconds)