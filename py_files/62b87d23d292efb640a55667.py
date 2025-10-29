def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def wrapper(self, *args, **kwargs):
		return getattr(self, method)(vcs, *args, **kwargs)
	return wrapper