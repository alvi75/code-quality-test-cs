def validate_key(key):
	"""
	Validate the given key against the corresponding regular expression.
	"""
	if not isinstance(key, str):
		raise TypeError("key must be a string")
	elif len(re.findall(r"\W", key)) > 0:
		raise ValueError("invalid characters in key")