def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LRU(maxsize) if maxsize is not None else {}
		if typed:
			cache = LRUTyped(maxsize)

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = args
			if kwargs:
				key += tuple(kwargs.items())
			try:
				result = cache[key]
			except KeyError:
				result = user_function(*args, **kwargs)
				cache[key] = result
			return result
		return wrapper
	return decorating_function