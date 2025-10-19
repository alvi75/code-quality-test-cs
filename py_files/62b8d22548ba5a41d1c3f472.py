def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(method):
		@wraps(method)
		def wrapper(self, *args, **kwargs):
			if not isinstance(cache, Cache):
				cache = Cache(cache)

			if lock is None:
				lock = self

			result = cache.get(key(self, *args, **kwargs), lock=lock)
			if result is None:
				result = method(self, *args, **kwargs)
				cache.set(key(self, *args, **kwargs), result, lock=lock)
			return result
		return wrapper
	return decorator