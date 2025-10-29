def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not os.path.exists('build'):
		return True

	for f in glob.glob(os.path.join('build', '*.o')):
		if not os.path.exists(f):
			return True

	return False