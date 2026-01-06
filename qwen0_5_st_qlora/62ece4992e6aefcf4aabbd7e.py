def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.group('name') in os.environ:
		return os.environ[matcher.group('name')]
	elif matcher.group('default'):
		return matcher.group('default')
	else:
		raise ValueError("No value for %s found in environment." % matcher.group('name'))