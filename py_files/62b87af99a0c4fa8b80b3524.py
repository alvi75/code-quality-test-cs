def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if hasattr(obj, 'run'):
		return True
	elif hasattr(obj, '__call__') and callable(obj.run):
		return True
	else:
		return False