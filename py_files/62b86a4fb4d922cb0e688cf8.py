def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not re.match(_REGEX[value], value):
		raise ValueError("Invalid value for %s: '%s'" % (value, value))