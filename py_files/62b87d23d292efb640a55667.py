def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def wrapper(obj):
		if not hasattr(obj, 'vcs'):
			obj.vcs = vcs

		if not hasattr(obj, 'register_vcs_handler'):
			obj.register_vcs_handler = {}

		obj.register_vcs_handler[method] = method

		return obj

	return wrapper