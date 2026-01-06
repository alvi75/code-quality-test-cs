def normalized(self):
	"""
	Normalize all units of time to integers.
	"""
	return {
		"seconds": self.seconds,
		"minutes": int(self.minutes),
		"hours": int(self.hours),
		"days": int(self.days),
	}