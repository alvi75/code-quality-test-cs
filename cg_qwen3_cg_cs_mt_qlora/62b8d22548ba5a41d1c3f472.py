def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def _cachedmethod(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			result = cache.get(key)
			if result is None:
				with lock:
					result = func(*args, **kwargs)
					cache.set(key, result)
			return result
		return wrapper
	return _cachedmethod