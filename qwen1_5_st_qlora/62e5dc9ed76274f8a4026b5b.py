def deprecated(message):
	"""
	Return a decorator function for deprecating functions and methods.
	"""
	def decorate(func):
		if inspect.ismethod(func) or inspect.isfunction(func):
			func.__deprecated__ = message

		return func
	return decorate