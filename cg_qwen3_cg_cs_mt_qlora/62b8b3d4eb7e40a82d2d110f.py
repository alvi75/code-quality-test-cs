def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not _c_optimizations:
		return False

	if _c_optimizations == 'auto':
		try:
			import numpy
		except ImportError:
			return False
		else:
			return True

	return _c_optimizations