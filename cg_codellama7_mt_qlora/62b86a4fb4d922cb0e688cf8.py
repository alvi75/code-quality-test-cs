def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, basestring):
		raise ValueError("Value must be a string")
	if not re.match(value_regex, value):
		raise ValueError("Value must be a valid string")