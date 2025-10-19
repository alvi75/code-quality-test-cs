def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU) algorithm.
	"""

	def decorator(func):
		cache = Cache(maxsize=maxsize, typed=typed)

		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs)
			if key in cache:
				return cache[key]
			result = func(*args, **kwargs)
			cache[key] = result
			return result

		wrapper.cache_clear = cache.clear
		return wrapper

	return decorator