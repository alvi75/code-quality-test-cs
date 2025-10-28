def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if sys.version_info[0] == 2:
		return True
	else:
		return False