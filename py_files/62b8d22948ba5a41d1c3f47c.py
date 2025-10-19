def get(self, key, default=None):
		"""
		If a key exists in the class, the value corresponding to the key is returned. Otherwise, default is returned.
		"""
		if hasattr(self, key) and getattr(self, key) is not None:
			return getattr(self, key)
		else:
			return default