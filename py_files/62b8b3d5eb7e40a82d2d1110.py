def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		import pyfftw
	except ImportError:
		return False

	if not hasattr(pyfftw, 'set_default_fft_wisdom'):
		return False

	return True