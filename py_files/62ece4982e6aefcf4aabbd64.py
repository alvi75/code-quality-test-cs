def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.isabs(path):
		path = os.path.abspath(path)
	if not os.path.isdir(path):
		raise Exception("Path is not a directory: %s" % path)

	while path.startswith(root):
		path = path[len(root):]
	return path