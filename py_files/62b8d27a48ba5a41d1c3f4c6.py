def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args[0])
			if not hasattr(cache, 'cache'):
				cache.cache = {}
			if lock is None:
				lock = Lock()
			with lock:
				result = cache.cache.get(key)
				if result is None:
					result = func(*args, **kwargs)
					cache.cache[key] = result
				return result
		return wrapper
	return decorator