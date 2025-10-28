def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.isabs(root):
		raise ValueError("root must be absolute")
	if not os.path.isabs(path):
		raise ValueError("path must be absolute")

	root = os.path.abspath(root)
	path = os.path.abspath(path)

	if path.startswith(root + os.sep):
		return path[len(root):]
	else:
		raise ValueError("Path %s does not start with root %s" % (path, root))