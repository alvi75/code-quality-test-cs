def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LRU(maxsize=maxsize, typed=typed)

		if not hasattr(cache, 'cache_info'):
			cache.cache_info = cache.info

		if not hasattr(cache, 'cache_clear'):
			cache.cache_clear = cache.clear

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = args
			if kwargs:
				key += tuple(sorted(kwargs.items()))
			try:
				return cache[key]
			except KeyError:
				value = user_function(*args, **kwargs)
				cache[key] = value
				return value
		wrapper.cache_info = cache.cache_info
		wrapper.cache_clear = cache.cache_clear
		return wrapper
	return decorating_function