def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""

	def _cache(func):
		cache = {}
		mru = []
		call_count = 0

		def wrapper(*args, **kwargs):
			key = args + tuple(sorted(kwargs.items()))
			if key not in cache:
				result = func(*args, **kwargs)
				cache[key] = result
				call_count += 1
				if call_count >= maxsize:
					del cache[mru.pop()]
			else:
				call_count += 1
				mru.append(key)
				while len(mru) > maxsize:
					del cache[mru.pop(0)]
			return cache[key]

		wrapper.cache_clear = lambda: None
		wrapper.cache_info = lambda: CacheInfo(call_count, len(cache), maxsize,
											   len(mru))
		wrapper.cache_prune = lambda: None
		wrapper.cache_get = lambda key: cache.get(key)

		return functools.update_wrapper(wrapper, func)

	return _cache