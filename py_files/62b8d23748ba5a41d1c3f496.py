def lfu_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Frequently Used (LFU)
algorithm.
	"""
	if not isinstance(maxsize, int) or maxsize < 0:
		raise ValueError('maxsize must be a non-negative integer')
	if maxsize == 0:
		return _no_cache

	def decorating_function(user_function):
		cache = LfuCache(maxsize=maxsize, typed=typed)

		@functools.wraps(user_function)
		def wrapper(*args, **kwargs):
			key = args
			if kwargs:
				key += tuple(sorted(kwargs.items()))
			try:
				result = cache[key]
			except KeyError:
				result = user_function(*args, **kwargs)
				cache.add(key, result)
			return result
		return wrapper
	return decorating_function