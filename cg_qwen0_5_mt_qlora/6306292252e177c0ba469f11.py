def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	if isinstance(dt, datetime.datetime):
		return dt.strftime('%Y-%m-%d %H:%M:%S')
	elif isinstance(dt, datetime.date):
		return dt.strftime('%Y-%m-%d')
	else:
		raise ValueError('Invalid type for dt: {}'.format(type(dt)))