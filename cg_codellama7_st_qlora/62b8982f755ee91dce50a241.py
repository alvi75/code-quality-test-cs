def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	if self.years:
		self.years = int(self.years)
	if self.months:
		self.months = int(self.months)
	if self.weeks:
		self.weeks = int(self.weeks)
	if self.days:
		self.days = int(self.days)
	if self.hours:
		self.hours = int(self.hours)
	if self.minutes:
		self.minutes = int(self.minutes)
	if self.seconds:
		self.seconds = int(self.seconds)
	if self.milliseconds:
		self.milliseconds = int(self.milliseconds)
	if self.microseconds:
		self.microseconds = int(self.microseconds)
	return self