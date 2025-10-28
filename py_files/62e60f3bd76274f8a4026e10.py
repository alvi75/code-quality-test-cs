def dehydrate_timedelta(value):
	"""
	Use the value in timedelta to generate the Structure class.
	"""
	if isinstance(value, datetime.timedelta):
		return {'days': value.days,
				'hours': value.seconds / 3600 % 24,
				'minutes': (value.seconds // 60) % 60,
				'seconds': value.seconds}
	else:
		raise ValueError('Value is not a valid timedelta')