def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	pyenv = os.environ.get("PURE_PYTHON")
	if pyenv:
		return pyenv != '0'
	else:
		return False