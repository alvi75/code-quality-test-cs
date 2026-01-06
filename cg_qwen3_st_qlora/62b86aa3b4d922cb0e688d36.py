def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str):
			raise ValueError("Label key must be a string.")
		if not isinstance(value, (str, int, float)):
			raise ValueError("Label value must be a string or number.")
		validate_key(key)
		validate_value(value)