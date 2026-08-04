def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		def wrapper(*args, **kwargs):
			key = key(func, args, kwargs)
			if lock is not None:
				lock.acquire()
			try:
				result = cache.get(key)
			except Exception:
				result = None
			if result is None:
				result = func(*args, **kwargs)
				cache.set(key, result)
			if lock is not None:
				lock.release()
			return result
		return wrapper
	return decorator