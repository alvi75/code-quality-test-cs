def _c_optimizations_available():
	"""
	If available, return the C optimization module, otherwise a false value.
	"""
	try:
		import pyximport
	except ImportError:
		return False

	try:
		# Try to import the c optimizations
		pyximport.install()
		from .optimizations import *
		return True
	except Exception as e:
		print("C optimizations failed: %s" % str(e))
		return False