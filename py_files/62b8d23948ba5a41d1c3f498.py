def lru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Least Recently Used (LRU)
algorithm.
	"""

	def decorating_function(user_function, *args, **kwds):
		if not isinstance(maxsize, int) or maxsize < 0:
			raise ValueError("maxsize must be a non-negative integer")
		if not isinstance(typed, bool):
			raise TypeError("typed must be a boolean")

		cache = dict()
		atimes = dict()

		def memoizer(*args, **kwds):
			key = args if typed else tuple(args)
			try:
				return cache[key]
			except KeyError:
				v = user_function(*args, **kwds)
				cache[key] = v
				atimes[key] = time()
				return v

		def cached_func(*args, **kwds):
			key = args if typed else tuple(args)
			if key in atimes and time() - atimes[key] > maxsize:
				del cache[key]
				del atimes[key]
			return memoizer(*args, **kwds)

		cached_func.cache_info = lambda: _get_cache_info(cache, atimes)
		cached_func.cache_clear = lambda: _clear_cache(cache, atimes)

		return functools.update_wrapper(cached_func, user_function)

	return decorating_function