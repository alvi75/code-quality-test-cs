def is_fill_compute_el(obj):
	"""
	Check whether the obj class has the fill and compute methods.
	"""
	return (
		obj.__class__.fill is not None and
		obj.__class__.compute is not None
	)