def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not re.match(VALIDATION_REGEXES[validate_type], value):
		raise ValueError("'%s' is not a valid %s" % (value, validate_type))