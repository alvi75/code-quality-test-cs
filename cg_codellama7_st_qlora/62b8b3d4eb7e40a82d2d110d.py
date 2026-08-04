def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not _c_optimizations_required.value:
		_c_optimizations_required.value = _c_optimizations_required_impl()
	return _c_optimizations_required.value