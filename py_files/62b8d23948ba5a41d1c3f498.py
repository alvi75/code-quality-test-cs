def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def decorator(func):
		cache = {}
		if typed:
			key = lambda x: x.__class__
		else:
			key = lambda x: id(x)

		def wrapper(*args, **kwargs):
			key_args = key(args) + tuple(kwargs.items())
			if key_args in cache:
				return cache[key_args]
			result = func(*args, **kwargs)
			cache[key_args] = result
			return result

		return wrapper

	return decorator