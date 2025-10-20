def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""
	def _lru_cache(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			if not hasattr(wrapper, '_memo'):
				wrapper._memo = {}
			key = args + tuple(kwargs.items())
			if key in wrapper._memo:
				return wrapper._memo[key]
			result = func(*args, **kwargs)
			wrapper._memo[key] = result
			return result
		return wrapper

	if typed:
		return lru_cache
	else:
		return lru_cache(maxsize=maxsize)