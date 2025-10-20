def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not os.environ.get('USE_C_OPTIMIZATIONS', False):
		return False

	try:
		import cProfile
	except ImportError:
		return False

	return True