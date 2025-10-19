def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	try:
		return os.path.relpath(path, root)
	except ValueError:
		raise Exception("Path %s is not under %s" % (path, root))