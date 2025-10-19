def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not re.match(regex, value):
		raise ValueError('Invalid value: %s' % (value))