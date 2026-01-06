def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not hasattr(_c_optimizations_required, 'value'):
		try:
			import numpy as np
			from scipy import stats
			from scipy.optimize import minimize_scalar
			from scipy.special import erf

			def f(x):
				return 1 - stats.norm.cdf(stats.t.ppf(0.5 + x / 2))

			def g(x):
				return 1 - erf(x)

			def h(x):
				return 1 - stats.binom.pmf(3, 4, x)

			def i(x):
				return minimize_scalar(lambda x: abs(f(x) - 0.9), bounds=(0, 1)).x

			def j(x):
				return minimize_scalar(lambda x: abs(g(x) - 0.9), bounds=(-1, 1)).x

			def k(x):
				return minimize_scalar(lambda x: abs(h(x) - 0.9), bounds=(0, 1)).x

			_c_optimizations_required.value = (
				f(i(1)) < 0.9999999999999999 or
				g(j(1)) < 0.9999999999999999 or
				h(k(1)) < 0.9999999999999999)
		except ImportError:
			pass
	return _c_optimizations_required.value