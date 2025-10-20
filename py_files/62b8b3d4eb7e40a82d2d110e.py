def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	environ = os.environ.copy()
	environ.pop('PURE_PYTHON', None)
	return environ.get('PURE_PYTHON') != '0'