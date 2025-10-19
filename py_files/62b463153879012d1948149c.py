def select_filenames_by_prefix(prefix, files):
	"""
	For each file in files, return all files taht match the given prefix
	"""
	files = list(files)
	prefix = os.path.normpath(prefix)

	for f in files:
		if os.path.basename(f) == prefix or \
			os.path.basename(f).startswith(prefix + '.') or \
			f.endswith('/%s' % prefix) or \
			f.endswith('/%s.' % prefix):
			yield f