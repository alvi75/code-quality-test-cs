def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if not hasattr(obj, 'run'):
		raise Exception('The object does not have a run method.')
	return True