def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorator(user_function):
		cache = lfu_cache_factory(maxsize, user_function, typed)

		if not typed:
			sig = signature(user_function)

		@wraps(user_function)
		def wrapper(*args, **kwargs):
			return cache(*args, **kwargs)

		wrapper.cache_info = cache_info = partial(cache, True)
		wrapper.cache_clear = cache_clear = partial(cache, False)

		return wrapper

	return decorator