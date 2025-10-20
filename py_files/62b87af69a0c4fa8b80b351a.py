def is_fill_compute_el(obj):
	"""
	Check whether the obj class has the fill and compute methods.
	"""
	return hasattr(obj, 'fill') and hasattr(obj, 'compute') and callable(getattr(obj, 'fill')) and callable(getattr(obj, 'compute'))