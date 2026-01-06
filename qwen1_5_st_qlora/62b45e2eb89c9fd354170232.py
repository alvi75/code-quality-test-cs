def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	pattern = re.compile(r'(\d+)(?:\.(\d+))?(?:\.(\d+))?(?:\.(\d+))?$')
	m = pattern.match(version)
	if not m:
		raise ValueError('Invalid version string: %s' % (version,))
	groups = m.groups()
	for i in range(1, len(groups)):
		group = groups[i]
		if group is None or group == '':
			continue
		try:
			group = int(group)
		except ValueError:
			pass
	return '%02d.%02d.%02d.%02d' % tuple([int(x) if x else 0 for x in groups])