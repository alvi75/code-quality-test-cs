def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""

	def decorating_function(f):
		cache = LFUCache(maxsize=maxsize, typed=typed)

		@wraps(f)
		def wrapper(*args, **kwargs):
			key = make_key(args, kwargs)
			if key not in cache:
				result = f(*args, **kwargs)
				cache[key] = result
			return cache[key]

		wrapper.cache_clear = cache.clear
		wrapper.cache_info = cache.info
		wrapper.cache_replace = cache.replace

		return wrapper

	return decorating_function