def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if re.match(VALID_KEYS[key], key) is None:
		raise ValueError("Invalid %s key: '%s'" % (key, key))
	return True