def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not HAVE_C_OPTIMIZATIONS:
		return False

	if sys.platform == 'win32':
		# On Windows, we can't use the C optimizations because of
		# https://bugs.python.org/issue18375
		return False

	if sys.version_info < (3, 0):
		# On Python 2, we can't use the C optimizations because of
		# https://bugs.python.org/issue19846
		return False

	if sys.version_info >= (3, 3) and sys.platform.startswith('linux'):
		# On Linux with Python 3.3 or later, we can't use the C
		# optimizations because of
		# https://bugs.python.org/issue20863
		return False

	return True