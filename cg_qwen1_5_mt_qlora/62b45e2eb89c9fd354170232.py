def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not isinstance(version, str):
		raise TypeError("Version must be a string")
	version = version.split('.')
	for i in range(len(version)):
		try:
			version[i] = int(version[i])
		except ValueError:
			pass
	return '.'.join(str(x+1) if x < len(version)-1 else '0' for x in version)