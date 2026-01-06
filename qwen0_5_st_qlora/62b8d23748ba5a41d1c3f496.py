def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def _lfu_cache(func):
		"""Memoize the result of func."""
		cache = {}
		def wrapper(*args, **kwargs):
			key = args + tuple(kwargs.items())
			if key in cache:
				return cache[key]
			elif len(cache) >= maxsize:
				del cache[cache.popitem()[0][0]]
			result = func(*args, **kwargs)
			cache[key] = result
			return result
		return wrapper
	return _lfu_cache