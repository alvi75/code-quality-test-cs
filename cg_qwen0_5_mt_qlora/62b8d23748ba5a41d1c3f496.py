def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def _lru_cache(func):
		"""Memoize the result of func."""
		def wrapper(*args, **kwargs):
			if not hasattr(wrapper, '_cache'):
				wrapper._cache = {}
			key = args + tuple(kwargs.items())
			if key in wrapper._cache:
				return wrapper._cache[key]
			result = func(*args, **kwargs)
			if typed:
				wrapper._cache[key] = result
			else:
				wrapper._cache[key] = result
			return result
		return wrapper
	return _lru_cache