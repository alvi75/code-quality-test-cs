def on(self, hook):
	"""
	Return a decorator function to add a new handler to the "hook" in the registry in the class.
	"""
	def _on(handler):
		self._registry[hook].append(handler)
		return handler

	return _on