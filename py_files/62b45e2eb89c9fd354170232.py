def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	version = re.sub(r'(\d+)(\D)', r'\1.\2', version)
	return int(version) + 1