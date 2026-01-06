def is_fill_request_el(obj):
	"""
	Check whether the obj class has the fill and request attributes.
	"""
	return hasattr(obj, 'fill') and hasattr(obj, 'request') and \
			hasattr(obj.fill, 'get') and hasattr(obj.request, 'get')