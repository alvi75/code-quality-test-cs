def is_fill_compute_el(obj):
	"""
	Check whether the obj class has the fill and compute methods.
	"""
	if not hasattr(obj, 'fill'):
		return False

	if not hasattr(obj.fill, '__call__'):
		return False

	if not hasattr(obj.compute, '__call__'):
		return False

	return True