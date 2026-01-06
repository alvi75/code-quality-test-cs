def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(self, *args, **kwargs):
			key = key(self, args, kwargs)
			result = cache.get(key)
			if result is None:
				with lock:
					result = func(self, *args, **kwargs)
					cache.set(key, result)
			return result
		return wrapper
	return decorator