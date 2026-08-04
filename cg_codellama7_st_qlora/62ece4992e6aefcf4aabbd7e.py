def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group('name')
	default = matcher.group('default')
	value = os.environ.get(name, default)
	if value is None:
		raise ValueError('Environment variable {} is not defined'.format(name))
	return value