def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		import _cmark._cmark as cmark
	except ImportError:
		return False

	if not cmark.CMARK_VERSION_INFO[0] >= 1 or \
			(cmark.CMARK_VERSION_INFO[0] == 1 and cmark.CMARK_VERSION_INFO[1] < 23):
		raise RuntimeError("The installed libmarkdown is too old to use the C extensions.")

	return cmark