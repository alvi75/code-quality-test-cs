def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		from . import c_optimizations
	except ImportError:
		return False
	else:
		return c_optimizations