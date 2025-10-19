def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if sys.platform == "win32":
		return False

	if not hasattr(sys, "_getframe"):
		return True

	f = sys._getframe(1)
	while f:
		if f.f_code.co_name == 'optimize':
			return True
		f = f.f_back
	return False