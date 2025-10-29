def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def _register(func):
		if vcs not in VCS_HANDLERS:
			VCS_HANDLERS[vcs] = {}
		VCS_HANDLERS[vcs][method] = func
		return func
	return _register