def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not _has_c_optimizations():
		return False
	if not _has_c_optimizations_enabled():
		return False
	if not _has_c_optimizations_available():
		return False
	return True