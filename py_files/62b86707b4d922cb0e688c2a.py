def on(self, hook):
	"""
	Return a decorator function to add a new handler to the "hook" in the registry in the class.
	"""
	def register(fn):
		if not hasattr(fn, "__hooks__"):
			fn.__hooks__ = []
		if hook not in fn.__hooks__:
			fn.__hooks__.append(hook)
		return fn
	return register