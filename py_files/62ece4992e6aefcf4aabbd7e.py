def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if 'default' in matcher:
		return os.environ.get(matcher['name'], matcher['default'])
	else:
		return os.environ.get(matcher['name'])