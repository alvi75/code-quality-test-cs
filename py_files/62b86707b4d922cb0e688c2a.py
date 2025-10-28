def on(self, hook):
	"""
	Return a decorator function to add a new handler to the "hook" in the registry in the class.
	"""
	def decorator(f):
		self.hooks[hook].append(f)
		return f

	return decorator