def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not hasattr(_c_optimizations_required, "value"):
		try:
			import numpy as np
			from scipy import stats
			from scipy.optimize import curve_fit
			from scipy.integrate import quad
			from scipy.special import erf

			# Check for the existence of the c-optimizations
			np.array([1])
			stats.norm.pdf(0)
			curve_fit(np.sin, [0], [0])
			quad(lambda x: 1 / (x ** 2 + 1), -1e30, 1e30)
			erf(0)

			# If all these things work then we can use the c-optimized functions
			_c_optimizations_required.value = True
		except ImportError:
			_c_optimizations_required.value = False
	return _c_optimizations_required.value