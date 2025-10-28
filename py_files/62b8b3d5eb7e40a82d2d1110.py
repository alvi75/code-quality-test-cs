def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		from scipy.optimize import minimize
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_slsq
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_bfgs
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_cobyla
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_cg
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_levenberg
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_nelemintrange
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_nelder_mead
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_trf
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_tnc
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gwls
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gsl
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gscipy
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gx
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxm
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxx
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa2
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa3
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa4
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa5
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa6
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa7
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa8
	except ImportError:
		return False

	try:
		from scipy.optimize import minimize_gxxgxa9
	except ImportError:
		return False

	try: