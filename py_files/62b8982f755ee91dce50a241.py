def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	return self._replace(
		seconds=self.seconds,
		minutes=self.minutes + (self.seconds // 60),
		hours=self.hours + (self.minutes // 60),
		days=self.days + (self.hours // 24),
	)