def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	return (
		__config__.c_optimization_level is not None or
		__config__.c_optimization_level == 0
	)