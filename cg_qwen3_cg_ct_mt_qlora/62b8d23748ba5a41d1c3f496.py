def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = LfuCache(maxsize=maxsize, typed=typed)
		if not hasattr(cache, 'cache_info'):
			cache.cache_info = cache.info
		if not hasattr(cache, 'cache_clear'):
			cache.cache_clear = lambda: None
		return functools.update_wrapper(cache(user_function), user_function)
	return decorating_function