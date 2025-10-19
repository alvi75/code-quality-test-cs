def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if not hasattr(obj, 'run'):
		return False

	if inspect.isclass(obj) and issubclass(obj, RunBase):
		return True
	else:
		return False