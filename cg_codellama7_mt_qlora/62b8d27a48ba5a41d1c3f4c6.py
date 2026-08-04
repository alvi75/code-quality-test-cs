def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			key = key(func, args, kwargs)
			if lock:
				with lock:
					if key in cache:
						return cache[key]
					result = func(*args, **kwargs)
					cache[key] = result
					return result
			else:
				if key in cache:
					return cache[key]
				result = func(*args, **kwargs)
				cache[key] = result
				return result
		return wrapper
	return decorator