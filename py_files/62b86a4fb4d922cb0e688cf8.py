def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, str):
		raise TypeError("value must be a string")
	if not re.match(r'^[0-9a-f]{24}$', value):
		raise ValueError("value is not a valid hex string")