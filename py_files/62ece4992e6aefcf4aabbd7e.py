def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group('name')
	default_value = None

	if 'default' in matcher.groups():
		default_value = matcher.group('default')

	return os.environ.get(name, default_value)