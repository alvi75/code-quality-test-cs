def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
	up to `maxsize` results based on a Least Frequently Used (LFU)
	algorithm.
	"""
	def decorating_function(user_function):
		cache = LFUCache(maxsize=maxsize, typed=typed)

		def wrapper(*args, **kwds):
			result = cache.get(args, kwds)
			if result is not None:
				return result

			result = user_function(*args, **kwds)
			cache[args, kwds] = result
			return result

		wrapper.cache_clear = cache.clear
		return update_wrapper(wrapper, user_function)

	return decorating_function