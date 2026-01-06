def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.exists(path):
		raise Exception("Path does not exist: %s" % path)
	if not os.path.isdir(path):
		raise Exception("Path is not a directory: %s" % path)

	return os.path.basename(os.path.dirname(path))