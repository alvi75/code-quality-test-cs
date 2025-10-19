def is_fill_request_el(obj):
	"""
	Check whether the obj class has the fill and request attributes.
	"""
	return (
		obj.__class__ is not str
		and hasattr(obj, "fill")
		and hasattr(obj, "request")
	)