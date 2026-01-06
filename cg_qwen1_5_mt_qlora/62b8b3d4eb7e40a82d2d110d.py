def _c_optimizations_required():
	"""
	Return a true value if the C optimizations are required.
	"""
	if not os.path.exists(os.path.join(_get_build_dir(), 'lib', 'pyglet.so')):
		return True

	try:
		with open(os.path.join(_get_build_dir(), 'include', 'pyglet.h')) as f:
			for line in f.readlines():
				line = line.strip()
				if line.startswith('#define PYGLET_VERSION_MAJOR'):
					major = int(line.split()[2])
					break
	except IOError:
		pass
	else:
		if major < 1065:
			return True

	return False