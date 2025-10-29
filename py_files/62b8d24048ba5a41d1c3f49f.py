def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def wrapper(func):
		cache = LRU(maxsize=maxsize, typed=typed)

		@functools.wraps(func)
		def wrapped(*args, **kwargs):
			key = _make_key(args, kwargs, typed)
			if key in cache:
				result, expires_at = cache[key]
				if timer() < expires_at:
					return result
				else:
					del cache[key]

			result = func(*args, **kwargs)
			cache[key] = (result, timer() + ttl)
			return result

		return wrapped
	return wrapper