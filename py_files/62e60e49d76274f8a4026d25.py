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
				timeout = 0

			with UnitOfWork(metadata=metadata, timeout=timeout) as uow:
				return func(uow, *args, **kwargs)

		return wrapper

	return decorator