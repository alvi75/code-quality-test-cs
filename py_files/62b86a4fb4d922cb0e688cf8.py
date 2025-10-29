def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, str):
		raise TypeError("value must be a string")
	if not re.match(r'^[a-zA-Z0-9_]+$', value):
		raise ValueError("value must only contain alphanumeric characters and underscores")