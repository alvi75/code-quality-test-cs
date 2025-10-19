def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if os.environ.get("C_OPTIMIZATIONS_REQUIRED") is not None:
		return bool(os.environ["C_OPTIMIZATIONS_REQUIRED"])
	else:
		return False