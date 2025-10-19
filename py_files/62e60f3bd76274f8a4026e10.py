def dehydrate_timedelta(value):
		"""
		Use the value in timedelta to generate the Structure class.
		"""
		return struct.Struct('!d', value.days, value.seconds, value.microseconds).unpack()
	
	if isinstance(value, datetime.timedelta):
		return dehydrate_timedelta(value)
	else:
		raise TypeError("Value must be a datetime.timedelta")