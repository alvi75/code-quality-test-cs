def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU) algorithm.
	"""
	def decorator(func):
		cache = _Cache(maxsize=maxsize, typed=typed)

		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs)
			if key not in cache:
				cache[key] = func(*args, **kwargs)
			return cache[key]
		wrapper.cache_clear = cache.clear
		return wrapper

	return decorator