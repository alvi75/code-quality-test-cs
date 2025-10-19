def is_run_el(obj):
	"""
	Check whether the obj class has the run method.
	"""
	if not isinstance(obj, type) or not hasattr(obj, '__mro__'):
		return False

	for cls in reversed(obj.__mro__):
		if hasattr(cls, 'run_el') and callable(getattr(cls, 'run_el')):
			return True

	return False