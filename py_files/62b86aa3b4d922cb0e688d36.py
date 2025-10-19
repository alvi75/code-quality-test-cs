def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str):
			raise TypeError("labels must be a dictionary of strings: {key:value,...}")
		if not isinstance(value, (str, int, float)):
			raise TypeError("labels must be a dictionary of strings: {key:value,...}")