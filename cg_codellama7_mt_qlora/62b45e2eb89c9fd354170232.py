def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if version.endswith('-dev'):
		return version[:-4] + '.dev0'
	else:
		return version + '.dev0'