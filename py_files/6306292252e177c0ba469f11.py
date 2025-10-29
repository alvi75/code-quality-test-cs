def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	if not isinstance(dt, datetime.datetime):
		dt = datetime.datetime.strptime(str(dt), '%Y-%m-%dT%H:%M:%S.%f')
	return ensure_timezone(dt)