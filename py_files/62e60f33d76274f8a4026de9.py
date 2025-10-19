def dehydrate_point(value):
		"""
		The structure class is generated based on the value length.
		"""
		if isinstance(value, int) or isinstance(value, float):
			return value
		elif isinstance(value, str):
			return value.encode('utf-8')
		else:
			raise ValueError("Value type not supported: %s" % type(value))

	return dehydrate_point