def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	if sys.platform == 'darwin':
		return False

	try:
		import c_optimizations
	except ImportError:
		return False
	else:
		return True