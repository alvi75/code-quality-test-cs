def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if not isinstance(key, str):
		raise TypeError("key must be a string")
	if not re.match(r'^[a-zA-Z0-9_]+$', key):
		raise ValueError("key must only contain alphanumeric characters, underscores and dashes")