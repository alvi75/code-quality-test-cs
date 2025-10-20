def _resolve_string(matcher):
	"""
	Get the value from environment given a matcher containing a name and an optional default value in its group dict.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
	"""
	if matcher.group(1) in env:
		return env[matcher.group(1)]
	elif matcher.group(2) is not None:
		raise ValueError("Environment variable %s not defined" % matcher.group(2))
	else:
		return None