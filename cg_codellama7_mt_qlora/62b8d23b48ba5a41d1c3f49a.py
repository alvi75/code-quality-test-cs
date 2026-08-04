def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently Used (MRU)
algorithm.
	"""
	def decorating_function(user_function):
		cache = OrderedDict()
		hits = [0]
		misses = [0]
		def wrapper(*args, **kwds):
			key = _make_key(args, kwds, typed)
			if key in cache:
				hits[0] += 1
				value = cache.pop(key)
				cache[key] = value
				return value
			misses[0] += 1
			if len(cache) == maxsize:
				cache.popitem(last=False)
			value = user_function(*args, **kwds)
			cache[key] = value
			return value
		def cache_info():
			"""Return the cache statistics."""
			return (len(cache), len(cache), hits[0], misses[0])
		def cache_clear():
			"""Clear the cache and cache statistics."""
			cache.clear()
			hits[0] = misses[0] = 0
		wrapper.cache_info = cache_info
		wrapper.cache_clear = cache_clear
		return wrapper
	return decorating_function