def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not HAVE_C:
		return False

	if sys.platform == 'win32':
		return True

	if sys.platform == 'darwin':
		return True

	if sys.platform.startswith('linux'):
		return True

	return False