def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""

	def decorator(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			if metadata is None:
				metadata = {}

			if timeout is None:
				timeout = 10

			with UnitOfWork(metadata=metadata, timeout=timeout) as w:

				return func(*args, **kwargs)

		return wrapper

	return decorator