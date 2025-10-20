def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			if metadata is None:
				metadata = {}
			if timeout is None:
				timeout = 10
			with _unit_of_work(metadata=metadata, timeout=timeout) as uow:
				return func(*args, **kwargs)
		return wrapper
	return decorator