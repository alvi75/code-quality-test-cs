def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			with lock:
				if key not in cache:
					cache[key] = func(*args, **kwargs)
				return cache[key]
		return wrapper
	return decorator