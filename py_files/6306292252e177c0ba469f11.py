def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	return ensure_timezone(time.mktime((int(dt.year), int(dt.month), int(dt.day),
			int(dt.hour), int(dt.minute), int(dt.second), 0, 0, -1)))