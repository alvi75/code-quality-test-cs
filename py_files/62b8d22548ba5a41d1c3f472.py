def cachedmethod(cache, key=hashkey, lock=None):
	"""
	Returns a decorator function that can call a result in the cache.
	"""

	def decorator(func):

		@wraps(func)
		def wrapper(*args, **kwargs):
			key = key(args, kwargs)

			if not hasattr(wrapper, 'cache'):
				wrapper.cache = {}

			if key in wrapper.cache:
				return wrapper.cache[key]

			result = func(*args, **kwargs)
			wrapper.cache[key] = result

			return result

		return wrapper

	return decorator