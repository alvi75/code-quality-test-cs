def register_vcs_handler(vcs, method):
		"""Create decorator to mark a method as the handler of a object
		"""
		if not hasattr(vcs, '_vcs_handlers'):
			vcs._vcs_handlers = {}
		vcs._vcs_handlers[method.__name__] = method
		return method

	return register_vcs_handler