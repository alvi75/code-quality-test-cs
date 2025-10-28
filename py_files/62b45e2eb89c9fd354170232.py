def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not version:
		return "1.0"
	version = version.split('.')
	version[2] = str(int(version[2]) + 1)
	return '.'.join(version)