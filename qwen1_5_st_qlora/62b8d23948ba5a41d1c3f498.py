def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""

	def decorating_function(f):
		cache = Cache(maxsize=maxsize, typed=typed)

		@wraps(f)
		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs)
			if key not in cache:
				result = f(*args, **kwargs)
				cache[key] = result
			return cache[key]

		wrapper.cache_clear = cache.clear
		wrapper.cache_info = cache.info
		wrapper.cache_get = cache.get

		return wrapper

	return decorating_function