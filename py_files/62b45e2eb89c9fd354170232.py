def next_version(version):
	"""
	Given next version identifier following existing pattern
	"""
	if re.match(r'^\d+.\d+.\d+$', version) is not None:
		return str(int(re.match(r'^(\d+).(\d+).(\d+)$', version).group(1))+1)+'.0.0'
	elif re.match(r'^\d+.\d+.\d+.\d+$', version) is not None:
		return str(int(re.match(r'^(\d+).(\d+).(\d+).(\d+)$', version).group(1))+1)+'.0.0.0'
	else:
		raise ValueError('Invalid version string provided')