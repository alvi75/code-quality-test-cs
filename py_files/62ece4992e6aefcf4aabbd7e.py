def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if 'name' in matcher:
		name = matcher['name']
	else:
		name = None

	if 'default' in matcher:
		default = matcher['default']
	else:
		default = None

	if name is None or (name != '' and name == ''):
		return os.environ.get(name)
	elif name in os.environ:
		return os.environ[name]
	else:
		if default is not None:
			return default
		raise ValueError('Environment variable %s is undefined.' % name)