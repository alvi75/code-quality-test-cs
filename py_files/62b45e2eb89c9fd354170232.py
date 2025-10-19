def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	version = str(version)
	if not version:
		return '0.1'
	elif version[0] == 'v':
		version = version[1:]
	else:
		version = 'v' + version

	# Remove leading zeroes from major/minor/patch
	major, minor, patch = version.split('.')
	major = int(major)
	minor = int(minor)
	patch = int(patch)

	# Increment patch number
	patch += 1
	if patch > 9:
		patch = 0
		minor += 1
		if minor > 9:
			minor = 0
			major += 1
			if major > 9:
				major = 0

	return '{major}.{minor}.{patch}'.format(
		major=major,
		minor=minor,
		patch=patch,
	)