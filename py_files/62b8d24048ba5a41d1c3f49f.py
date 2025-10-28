def ttl_cache(maxsize=128, ttl=600, timer=time.monotonic, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
	up to `maxsize` results based on a Least Recently Used (LRU)
	algorithm with a per-item time-to-live (TTL) value.
	"""
	def decorating_function(user_function):
		cache = LRU(maxsize=maxsize)

		def wrapped(*args, **kwds):
			key = _make_key(args, kwds, typed=typed)
			if key in cache:
				result = cache[key]
			else:
				result = user_function(*args, **kwds)
				cache[key] = result

			now = timer()
			for k in list(cache.keys()):
				if now - cache[k][1] > ttl:
					del cache[k]

			return result

		wrapped.cache_clear = lambda: cache.clear()

		return functools.update_wrapper(wrapped, user_function)

	return decorating_function