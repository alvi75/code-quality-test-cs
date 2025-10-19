def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	pure_python = os.environ.get("PURE_PYTHON")
	if pure_python:
		return bool(pure_python) and int(pure_python)
	return False