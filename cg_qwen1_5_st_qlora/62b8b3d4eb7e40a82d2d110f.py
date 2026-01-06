def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	return (not os.environ.get('NO_C_OPTIMIZATIONS', False) and
			not os.environ.get('NO_C_OPTIMIZATIONS_FOR_PYTHON', True))