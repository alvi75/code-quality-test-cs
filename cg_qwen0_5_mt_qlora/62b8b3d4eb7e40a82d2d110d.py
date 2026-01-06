def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not __jit_enabled__:
		return False

	# Check for C optimizations that are not supported by the current
	# compiler version.
	for opt in ['-O0', '-O1', '-O2', '-O3']:
		if not __has_c_optimization(opt):
			return True

	return False