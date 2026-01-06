def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def _mru_cache(func):
		"""Memoize the result of func."""
		cache = {}
		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			if key in cache:
				return cache[key]
			result = func(*args, **kwargs)
			if typed:
				cache[key] = result
			else:
				cache[key] = result
			return result
		return wrapper
	return _mru_cache