def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""

	def wrapper(self, *args, **kwargs):
		return vcs.call_method(method, self, args, kwargs)

	wrapper.__name__ = method.__name__
	wrapper.__doc__ = method.__doc__

	return wrapper