def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def _cached(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			if key not in cache:
				cache[key] = func(*args, **kwargs)
			return cache[key]
		return wrapper
	return _cached