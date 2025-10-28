def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if not re.match(_KEY_REGEX, key):
		raise ValueError("Invalid key: %s" % key)