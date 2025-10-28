def make_find_paths(find_paths):
	"""
	Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path
	"""
	if isinstance(find_paths, basestring):
		find_paths = [find_paths]
	return tuple(map(lambda x: os.path.join(x) if not os.path.isabs(x) else x, find_paths))