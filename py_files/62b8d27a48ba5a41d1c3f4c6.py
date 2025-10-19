def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			k = key(args, kwargs)
			if k not in cache:
				with lock:  # if there is a lock
					if k not in cache:
						cache[k] = func(*args, **kwargs)
			return cache[k]
		return wrapper
	return decorator