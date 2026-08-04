def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			with cache.lock(key, lock):
				if key in cache:
					return cache[key]
				result = func(*args, **kwargs)
				cache[key] = result
				return result
		return wrapper
	return decorator