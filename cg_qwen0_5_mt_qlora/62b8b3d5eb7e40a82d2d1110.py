def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		return importlib.util.find_spec('cffi')
	except ImportError:
		return False