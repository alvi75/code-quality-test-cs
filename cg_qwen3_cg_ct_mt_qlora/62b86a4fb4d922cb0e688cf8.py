def validate_value(value):
	"""
	Validate the given value against the corresponding regular expression.
	"""
	if not isinstance(value, str):
		raise ValueError("Value must be a string")

	for regex in REGEXES:
		if re.match(regex[0], value):
			return

	raise ValueError("Invalid value")