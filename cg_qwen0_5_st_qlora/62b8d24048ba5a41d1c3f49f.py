def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorator(func):
		cache = _Cache(maxsize=maxsize, ttl=ttl, timer=timer, typed=typed)

		def wrapper(*args, **kwargs):
			key = args + tuple(kwargs.items())
			if key not in cache:
				result = func(*args, **kwargs)
				cache[key] = result
			return cache[key]
		return wrapper
	return decorator