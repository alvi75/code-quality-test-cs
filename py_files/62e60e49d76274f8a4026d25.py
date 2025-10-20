def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""

	def decorator(func):

		if not hasattr(func, 'metadata'):
			func.metadata = {}

		if metadata is None:
			metadata = {}
		else:
			metadata = dict(metadata)

		if timeout is None:
			timeout = 0

		func.timeout = timeout
		func.metadata.update(metadata)
		return func

	return decorator