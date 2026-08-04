def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			with UnitOfWork(metadata=metadata, timeout=timeout):
				return func(*args, **kwargs)
		return wrapper
	return decorator