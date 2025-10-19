def on(self, hook):
	"""
	Return a decorator function to add a new handler to the "hook" in the registry in the class.
	"""

	def _on(handler):

		if not hasattr(self.__class__, self.HOOKS_ATTRIBUTE_NAME):
			self.__class__.__setattr__(self.HOOKS_ATTRIBUTE_NAME, {})

		hooks = getattr(self.__class__, self.HOOKS_ATTRIBUTE_NAME)
		if hook not in hooks:
			hooks[hook] = []

		hooks[hook].append(handler)
		return handler

	return _on