def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		if not hasattr(func, '_cache'):
			func._cache = {}
		cache_key = key(func)
		if cache_key not in func._cache:
			with (lock or Lock()):
				if cache_key not in func._cache:
					func._cache[cache_key] = func()
		return func._cache[cache_key]
	return decorator