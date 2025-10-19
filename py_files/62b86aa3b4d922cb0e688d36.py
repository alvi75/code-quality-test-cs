def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, str) or len(key) > 256:
			raise ValueError("Label key must be a string of at most 256 characters.")
		if not isinstance(value, (str, int, float)):
			raise TypeError("Label value must be a string, integer, or float.")