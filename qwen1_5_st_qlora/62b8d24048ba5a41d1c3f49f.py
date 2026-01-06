def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm with a per-item time-to-live (TTL) value.
	"""

	def decorating_function(f):

		cache = LRUCache(maxsize=maxsize, typed=typed)

		@wraps(f)
		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs)
			try:
				return cache[key]
			except KeyError:
				value = f(*args, **kwargs)
				cache[key] = value
				return value

		wrapper.cache_clear = cache.clear
		wrapper.cache_info = cache.info
		wrapper.cache_set = cache.set
		return wrapper

	return decorating_function