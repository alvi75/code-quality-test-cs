def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	if maxsize is None:
		maxsize = sys.maxsize

	def decorating_function(user_function):
		cache = dict()
		lru = LRU(maxsize)

		def wrapper(*args, **kwargs):
			key = args
			if typed:
				key += (type(arg) for arg in args)
			if kwargs:
				key += tuple(sorted(kwargs.items()))
			try:
				return lru.get(cache[key])
			except KeyError:
				result = user_function(*args, **kwargs)
				lru.put(cache[key], result)
				return result
		wrapper.cache_info = cache_info
		wrapper.cache_clear = cache_clear
		return wrapper
	return decorating_function