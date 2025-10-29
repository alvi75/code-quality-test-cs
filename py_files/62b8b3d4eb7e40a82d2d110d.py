def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not os.path.exists(_C_OPTIMIZATIONS):
		return False

	with open(_C_OPTIMIZATIONS, 'r') as f:
		for line in f:
			line = line.strip()
			if line.startswith('#'):
				continue
			if line.startswith('no-optimization'):
				return True
	return False