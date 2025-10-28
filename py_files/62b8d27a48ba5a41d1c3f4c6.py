def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def _cached(func):
		if not isinstance(cache, Cache):
			raise TypeError("cache must be an instance of Cache")
		cache = cache()
		key = key or hashkey

		def wrapper(*args, **kwargs):
			result = func(*args, **kwargs)
			if result is None:
				return result
			else:
				try:
					value = cache.get(key(args))
				except Exception as e:
					log.error(e)
					value = None
				if value is None:
					cache.set(key(args), result)
					return result
				elif lock:
					with lock():
						if cache.get(key(args)) != result:
							cache.set(key(args), result)
							return result
				return value
		return wrapper
	return _cached