def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	return Time(
		self.hour * 3600 + self.minute * 60 + self.second,
		self.microsecond)