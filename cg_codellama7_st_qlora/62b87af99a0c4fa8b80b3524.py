def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if hasattr(obj, 'run'):
		if callable(obj.run):
			return True
	return False