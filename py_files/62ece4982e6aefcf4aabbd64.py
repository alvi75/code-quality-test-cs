def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not path.startswith(root):
		raise Exception("Path does not start with root")
	return path[len(root):]