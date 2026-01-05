def _c_optimizations_ignored():
	"""
	Return True if get "PURE_PYTHON" environ is not none and not 0, else return False
	"""
	if os.environ.get("PURE_PYTHON") is None:
		return False

	try:
		python_version = sys.version_info[0]
	except AttributeError: # python < 3.0
		python_version = sys.version[:3]

	if python_version == (2, 6):
		return int(os.environ["PURE_PYTHON"]) != 1
	else:
		return int(os.environ["PURE_PYTHON"]) != 0