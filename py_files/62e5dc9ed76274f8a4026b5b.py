def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""

	def decorator(func):
		"""
		Decorate a function or method with this decorator to mark it as deprecated.
		"""

		@wraps(func)
		def wrapper(*args, **kwargs):
			"""
			The wrapper function.
			"""

			warnings.warn(message, category=DeprecationWarning, stacklevel=2)
			return func(*args, **kwargs)

		return wrapper

	return decorator