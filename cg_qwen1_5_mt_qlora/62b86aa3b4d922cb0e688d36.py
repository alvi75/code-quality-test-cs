def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str) or not isinstance(value, str):
			raise ValueError("Labels must be a dictionary of strings.")
		_validate_key(key)
		_validate_value(value)