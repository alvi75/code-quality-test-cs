def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""
	if not os.path.exists(root):
		raise Exception("Root does not exist: %s" % root)
	return os.path.normpath(os.path.join(root, path))