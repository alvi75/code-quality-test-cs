def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def _cachedmethod(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			if not cache.has(key):
				with lock:
					if not cache.has(key):
						result = func(*args, **kwargs)
						cache.set(key, result)
						return result
			else:
				return cache.get(key)
		return wrapper
	return _cachedmethod