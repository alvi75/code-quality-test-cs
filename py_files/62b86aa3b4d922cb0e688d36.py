def _validate_labels(labels):
	"""
	Check that keys and values in the given labels by validate_key() and validate_value().
	"""
	for label in labels:
		if not validate_key(label):
			raise ValueError("Invalid key: %s" % label)
		if not validate_value(label):
			raise ValueError("Invalid value: %s" % label)