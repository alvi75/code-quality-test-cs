def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not isinstance(key, six.string_types) or not isinstance(value, six.string_types):
			raise ValueError("Labels must be strings")
		if not isinstance(key, six.string_types):
			raise TypeError("Labels must be strings")