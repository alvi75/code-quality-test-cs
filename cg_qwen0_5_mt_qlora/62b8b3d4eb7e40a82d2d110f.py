def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not __jit_enabled__:
		return False

	# We can't do any of these optimizations in C, so we need to check for them
	# in Python.
	for opt in ['-O0', '-O1', '-O2', '-O3']:
		if opt in sys.argv:
			return True

	return False