def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	if os.environ.get("PURE_PYTHON") is None:
		return False

	try:
		python_version = sys.version_info[0]
	except AttributeError: # pragma: no cover
		return False

	if python_version < 3:
		return int(os.environ["PURE_PYTHON"]) != 1
	else:
		return int(os.environ["PURE_PYTHON"]) == 1