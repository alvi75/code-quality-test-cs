def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	python = os.environ.get("PURE_PYTHON")
	if python:
		return int(python) == 0
	else:
		return False