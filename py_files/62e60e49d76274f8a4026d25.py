def unit_of_work(metadata=None, timeout=None):
	"""
	Returns a decorator with metadata and timeout attributes.
	"""

	def _unit_of_work(func):

		func.metadata = metadata or {}
		func.timeout = timeout

		return func

	return _unit_of_work