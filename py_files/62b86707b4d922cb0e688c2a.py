def on(self, hook):
		"""
		Return a decorator function to add a new handler to the "hook" in the registry in the class.
		"""
		def _on(func):
			self._registry[hook].append(func)
			return func

		return _on