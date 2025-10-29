def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not isinstance(version, Version):
		version = Version(version)
	if version.is_prerelease:
		return next_prerelease(version)
	else:
		return next_release(version)