def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def wrapper(func):
		func.vcs = vcs
		return func
	return wrapper