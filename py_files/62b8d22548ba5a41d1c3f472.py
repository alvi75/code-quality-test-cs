def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args[0])
			if not hasattr(wrapper, '_cache'):
				wrapper._cache = cache
			if lock is None:
				lock = cache.lock
			with lock:
				result = func(*args, **kwargs)
				if result is not None:
					cache.set(key, result)
			return result
		return wrapper
	return decorator