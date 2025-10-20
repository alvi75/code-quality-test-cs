def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.isabs(path):
		raise ValueError("Path must be absolute")
	if not os.path.isabs(root):
		raise ValueError("Root must be absolute")

	if not path.startswith(root):
		raise ValueError("Path does not start with root")

	return path[len(root):]