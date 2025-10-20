def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for key, value in labels.items():
		if not validate_key(key):
			raise ValueError("Invalid label key: %s" % key)
		if not validate_value(value):
			raise ValueError("Invalid label value: %s" % value)