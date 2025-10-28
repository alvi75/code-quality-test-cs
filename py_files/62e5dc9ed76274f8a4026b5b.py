def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""

	def wrapper(func):
		if not hasattr(func, '__deprecated__'):
			func.__deprecated__ = True

		return func

	return wrapper