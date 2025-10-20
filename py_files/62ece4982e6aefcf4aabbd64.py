def strip_root(path, root):
	"""
	Remove root from path. If fails, throw exception

    Returns:
        A path without root
	"""

	if not os.path.isabs(root):
		root = os.path.abspath(root)

	try:
		return os.path.relpath(path, root)
	except ValueError as e:
		raise ValueError("Path %s is not under root %s" % (path, root))