def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, str):
		raise ValueError("Value must be a string")
	if not re.match(regex, value):
		raise ValueError("Value does not match regex")