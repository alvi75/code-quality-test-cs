def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not os.environ.get('NO_C_OPTIMIZATIONS'):
		return True

	for opt in os.environ.get('C_OPTIMIZATIONS', '').split(','):
		if opt == 'no':
			return False
	return True