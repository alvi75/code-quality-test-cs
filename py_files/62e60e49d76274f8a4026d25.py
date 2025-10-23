def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""
	def decorator(func):
		func.metadata = metadata
		func.timeout = timeout
		return func
	return decorator