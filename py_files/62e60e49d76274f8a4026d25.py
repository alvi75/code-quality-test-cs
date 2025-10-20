def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""
	def decorator(f):
		f.metadata = metadata or {}
		f.timeout = timeout or 0
		return f
	return decorator