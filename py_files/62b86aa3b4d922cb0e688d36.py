def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str) or not isinstance(value, str):
			raise ValueError("Labels must be strings")
		if len(key) == 0:
			raise ValueError("Labels cannot be empty strings")
		if len(value) == 0:
			raise ValueError("Labels cannot be empty strings")