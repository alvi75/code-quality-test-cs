def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			with lock:
				result = cache.get(key)
				if result is None:
					result = func(*args, **kwargs)
					cache.set(key, result)
			return result
		return wrapper
	return decorator