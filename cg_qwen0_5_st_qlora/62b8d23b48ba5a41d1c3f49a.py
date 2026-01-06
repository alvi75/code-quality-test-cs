def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorator(func):
		cache = {}
		if not typed:
			key = lambda x: x.__name__
		else:
			key = lambda x: x

		def wrapper(*args, **kwargs):
			key = key(args[0])
			if key in cache:
				return cache[key]
			result = func(*args, **kwargs)
			cache[key] = result
			return result
		wrapper.cache = cache
		return wrapper
	return decorator