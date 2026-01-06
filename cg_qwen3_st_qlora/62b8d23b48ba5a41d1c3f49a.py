def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LRUCache(maxsize, typed)
		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = args if not kwargs else args + tuple(kwargs.items())
			try:
				result = cache[key]
			except KeyError:
				result = user_function(*args, **kwargs)
				cache[key] = result
			return result
		return wrapper
	return decorating_function