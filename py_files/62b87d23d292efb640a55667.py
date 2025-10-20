def register_vcs_handler(vcs, method):
	"""
	Create decorator to mark a method as the handler of a object
	"""
	def wrapper(*args, **kwargs):
		vcs = vcs()
		return vcs._handler(method)
	return wrapper