def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	import sys, platform, os

	if sys.platform == 'darwin':
		return True
	elif sys.platform == 'linux2' or sys.platform == 'linux3':
		return False
	else:
		raise RuntimeError("Unknown platform: %s" % sys.platform)