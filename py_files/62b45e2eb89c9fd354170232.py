def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not version:
		version = '0.1'
	while True:
		version = str(int(version) + 1)
		if re.match(r'^[0-9]+\.[0-9]+\.[0-9]+$', version):
			break
	return version