def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def _cachedmethod(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			key = func.__name__ + str(args) + str(kwargs)
			if not isinstance(key, basestring):
				key = str(key)
			result = cache.get(key)
			if result is None:
				result = func(*args, **kwargs)
				cache.set(key, result, timeout=lock.timeout if lock else 0)
			return result
		return wrapper
	return _cachedmethod