def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorator(fn):
		cache = _memoize_typed_dict_lru(maxsize, timer, typed)

		@functools.wraps(fn)
		def wrapper(*args, **kwargs):
			return cache(fn, *args, **kwargs)

		wrapper.cache_info = cache.info
		wrapper.cache_clear = cache.clear

		return wrapper
	return decorator