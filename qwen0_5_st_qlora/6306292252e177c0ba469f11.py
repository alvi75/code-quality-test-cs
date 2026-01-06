def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	if not isinstance(dt, datetime.datetime):
		dt = datetime.datetime.strptime(str(dt), '%Y-%m-%d %H:%M:%S')
	return ensure_timezone(dt).strftime('%H:%M:%S')