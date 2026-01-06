def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def _memoize(func):
		"""Memoize the decorated function."""
		cache = {}
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			if key in cache:
				return cache[key]
			result = func(*args, **kwargs)
			if typed:
				result = result.__class__(result)
			if maxsize > 0 and len(cache) >= maxsize:
				expired = [k for k, v in cache.items() if v < timer()]
				for k in expired:
					del cache[k]
			cache[key] = result
			return result
		return wrapper
	return _memoize