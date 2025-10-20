def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		from cffi import FFI
		return True
	except ImportError:
		return False