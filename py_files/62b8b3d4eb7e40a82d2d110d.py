def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not sys.platform.startswith("win"):
		return False

	if os.environ.get("PYBLISH_QML_NO_C_OPTIMIZATIONS", None) is not None:
		return False

	if "PyInstaller" in sys.executable:
		return False

	import platform
	return platform.python_implementation() == "PyPy"