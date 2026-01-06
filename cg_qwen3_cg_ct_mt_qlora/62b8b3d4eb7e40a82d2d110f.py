def _should_attempt_c_optimizations():
	"""
	Return a true value if we use the C optimizations.
	"""
	if not _has_c_optimizations:
		return False

	if _c_optimizations_enabled is None:
		try:
			import numpy as np
		except ImportError:
			# No numpy, no c optimizations
			_c_optimizations_enabled = False
		else:
			# We have numpy, check for the right version
			_c_optimizations_enabled = (np.__version__ >= '1.8')

	return _c_optimizations_enabled