def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorator(func):
		cache = Cache(maxsize=maxsize, ttl=ttl, timer=timer, typed=typed)

		def wrapper(*args, **kwargs):
			key = _key(args, kwargs)
			result = cache.get(key)
			if result is None:
				result = func(*args, **kwargs)
				cache.set(key, result)
			return result

		return wrapper

	return decorator