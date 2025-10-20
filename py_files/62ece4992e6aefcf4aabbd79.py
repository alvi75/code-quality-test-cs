def make_find_paths(find_paths):
	"""
	Given a sequence of path, transform all path into glob patterns. Pass through existing patterns untouched.

    Args:
        find_paths: sequence of path
    Returns:
        tuple of transformed path
	"""
	return tuple(
		pattern if pattern.startswith('/') or pattern.startswith('*') else '{}/**'.format(pattern)
		for pattern in find_paths
	)