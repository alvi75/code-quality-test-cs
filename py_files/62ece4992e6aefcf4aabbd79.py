def make_find_paths(find_paths):
	"""
	Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path
	"""
	if not isinstance(find_paths, (list, tuple)):
		raise TypeError("find_path must be list or tuple")

	for i, path in enumerate(find_paths):
		if os.path.isdir(path) and not path.endswith(os.sep):
			find_paths[i] = "%s*" % path
		elif not fnmatch.is_valid_pattern(path):
			find_paths[i] = "*%s*" % path

	return find_paths