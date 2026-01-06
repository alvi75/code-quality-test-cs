def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def wrapper(func):
		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = key(args, kwargs)
			if lock is not None:
				with lock:
					return cache.get(key)
			else:
				return cache.get_or_set(key, func, timeout=cache_timeout)
		return wrapped
	return wrapper