def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not isinstance(version, Version):
		version = Version(version)
	return Version(next_version_str(version))