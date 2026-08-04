def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, basestring):
		raise TypeError("value must be a string")
	if not isinstance(value, unicode):
		value = value.decode('utf-8')
	if not re.match(regex, value):
		raise ValueError("value must match the regular expression %s" % regex)
	return value