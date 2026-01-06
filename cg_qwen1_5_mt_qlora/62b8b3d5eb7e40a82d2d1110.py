def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		import pyximport as pyximport
	except ImportError:
		return False

	pyximport.install()
	return True