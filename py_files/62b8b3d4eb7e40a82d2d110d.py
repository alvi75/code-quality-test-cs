def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	return (
		__C_OPTIMIZATION_REQUIRED or
		__C_OPTIMIZATION_REQUIRED_FOR_PTHREADS or
		__C_OPTIMIZATION_REQUIRED_FOR_PTHREADS_AND_PTHREADS
	)