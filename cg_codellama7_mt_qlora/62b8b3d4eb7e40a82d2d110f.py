def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not _c_optimizations_enabled:
		return False
	if _c_optimizations_enabled == 'auto':
		return _is_c_optimizations_enabled()
	return _c_optimizations_enabled