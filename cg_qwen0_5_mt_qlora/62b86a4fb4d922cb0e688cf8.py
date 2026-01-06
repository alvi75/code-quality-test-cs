def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, six.string_types):
		raise TypeError("value should be a string, but was %s" % type(value))
	if not re.match(r'^[a-zA-Z0-9_]+$', value):
		raise ValueError("value should only contain letters, numbers, and underscores")