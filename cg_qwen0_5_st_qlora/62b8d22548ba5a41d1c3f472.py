def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""

	def wrapper(func):
		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = key(args, kwargs)
			if not hasattr(wrapped, '_cache'):
				wrapped._cache = {}
			if key in wrapped._cache:
				return wrapped._cache[key]
			result = func(*args, **kwargs)
			if lock is not None:
				with lock:
					wrapped._cache[key] = result
			return result
		return wrapped
	return wrapper