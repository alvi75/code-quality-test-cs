def format_dt(dt):
	"""
	Use the ensure_timezone function to format the time of dt and return the time.
	"""
	if dt is None:
		return None

	if isinstance(dt, datetime.datetime):
		return dt.isoformat()
	elif isinstance(dt, datetime.date):
		return dt.strftime('%Y-%m-%d')
	else:
		raise TypeError('Invalid type for format_dt: %s' % type(dt))