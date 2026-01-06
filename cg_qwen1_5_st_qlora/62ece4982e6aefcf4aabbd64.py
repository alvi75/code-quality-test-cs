def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.isabs(root) or not os.path.isdir(root):
		raise ValueError("Root must be absolute directory")

	path = os.path.abspath(path)
	root = os.path.abspath(root)

	if not path.startswith(root):
		return None

	return path[len(root):]