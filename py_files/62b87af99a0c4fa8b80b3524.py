def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if not hasattr(obj, 'run'):
		return False
	else:
		return True