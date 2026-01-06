def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, basestring):
		raise TypeError("value must be a string")
	return re.match(_REGEXES[_TYPE], value) is not None