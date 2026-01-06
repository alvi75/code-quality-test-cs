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
			value = cache.get(key)
			if value is None:
				value = func(*args, **kwargs)
				cache[key] = (value, timer() + ttl)
			elif timer() < cache[key][1]:
				return cache[key][0]
			else:
				del cache[key]
			return value

		return wrapped

	return wrapper