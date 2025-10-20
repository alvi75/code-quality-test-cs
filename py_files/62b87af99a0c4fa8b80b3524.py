def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if hasattr(obj, 'run'):
		return True
	else:
		try:
			obj.run = getattr(obj.__class__, 'run')
			return True
		except AttributeError:
			pass
	return False