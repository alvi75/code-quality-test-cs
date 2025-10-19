def dehydrate_time(value):
		"""
		Use ticks in the Time class to generate the Structure class.
		"""
		if isinstance(value, Time):
			return value.ticks
		elif isinstance(value, int):
			return value
		else:
			raise TypeError("Time must be a Time or integer")
	
	return dehydrate_time