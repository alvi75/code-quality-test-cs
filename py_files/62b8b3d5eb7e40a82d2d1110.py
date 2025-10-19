def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		from . import c
	except ImportError:
		return False

	if not hasattr(c, "optimize"):
		return False

	return True