def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if sys.version_info[0] < 3:
		return True
	else:
		return False