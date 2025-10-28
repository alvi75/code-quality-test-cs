def cached(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that saves the results in the cache
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)
			if not hasattr(wrapper, 'cache'):
				wrapper.cache = cache

			if lock is None:
				lock = cache.lock

			with lock:
				result = wrapper.cache.get(key)

			if result is None:
				result = func(*args, **kwargs)
				wrapper.cache.set(key, result)

			return result

		return wrapper

	return decorator