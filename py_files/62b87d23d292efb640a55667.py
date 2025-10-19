def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def decorate(handler):
		"""
		Decorator that adds a new handler for vcs objects
		"""
		if not hasattr(handler, "handlers"):
			handler.handlers = {}
		if not isinstance(method, (list, tuple)):
			method = [method]
		for m in method:
			handler.handlers[m] = vcs
		return handler
	return decorate