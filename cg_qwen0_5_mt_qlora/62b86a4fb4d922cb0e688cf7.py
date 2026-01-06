def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if not isinstance(key, six.string_types):
		raise TypeError("key must be a string")
	if not re.match(r'^[a-zA-Z0-9_]+$', key):
		raise ValueError("key must only contain letters, numbers, underscores, and dashes")