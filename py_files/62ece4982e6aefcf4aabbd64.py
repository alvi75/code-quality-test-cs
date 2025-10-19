def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not path.startswith(root) or len(path) == 0:
		raise ValueError("Invalid path: %s" % path)
	return path[len(root):]