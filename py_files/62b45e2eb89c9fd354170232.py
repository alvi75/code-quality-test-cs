def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if not version:
		return '0.0.0'

	match = re.match(r'(\d+)\.(\d+)\.(\d+)', version)
	if match:
		return '%s.%s.%s' % (match.group(1) + 1, match.group(2), match.group(3))
	else:
		return '0.0.0'