def on(self, hook):
	"""
	Return a decorator function to add a new handler to the "hook" in the registry in the class.
	"""
	def decorator(func):
		self._hooks[hook].append(func)
		return func
	return decorator