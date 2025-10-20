def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str) or not isinstance(value, str):
			raise TypeError("labels must be a dict of strings")
		try:
			key = validate_key(key)
			value = validate_value(value)
		except Exception as e:
			raise TypeError("label '%s' is invalid: %s" % (key, e))
	return labels