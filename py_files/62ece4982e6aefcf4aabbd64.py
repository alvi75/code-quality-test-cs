def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.isabs(root) or not os.path.isabs(path):
		raise ValueError("Path must be absolute")

	return os.path.relpath(os.path.join(*os.path.split(path)[1:]), root)