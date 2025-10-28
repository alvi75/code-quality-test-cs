def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	return datetime.datetime.strftime(ensure_timezone(dt), '%H:%M')