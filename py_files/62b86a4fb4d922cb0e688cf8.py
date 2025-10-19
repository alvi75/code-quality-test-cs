def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, six.string_types):
		raise TypeError("value must be a string")
	return re.match(_REGEXES[validate_type(value)], value) is not None