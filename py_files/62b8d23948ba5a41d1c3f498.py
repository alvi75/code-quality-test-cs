def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LRU(maxsize) if maxsize is not None else {}
		if not typed:
			cache.keys = cache.keys() # typed=True changes this to be typed
		def wrapper(*args, **kwds):
			key = args
			if kwds:
				key += tuple(sorted(kwds.items()))
			try:
				result = cache[key]
			except KeyError:
				result = user_function(*args, **kwds)
				cache[key] = result
			return result
		wrapper.cache_info = cache.info
		wrapper.cache_clear = cache.clear
		return wrapper
	return decorating_function