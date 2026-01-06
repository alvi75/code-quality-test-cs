def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	name = matcher.group('name')
	default_value = None

	if 'default' in matcher.groupdict():
		default_value = matcher.group('default')

	try:
		value = os.environ[name]
	except KeyError:
		if default_value is None:
			raise EnvironmentError("Environment variable '%s' is required" % name)
		else:
			return default_value

	return value