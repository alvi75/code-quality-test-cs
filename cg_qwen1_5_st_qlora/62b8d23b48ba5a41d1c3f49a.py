def mru_cache(maxsize=128, typed=False):
	"""
	Decorator to wrap a function with a memoizing callable that saves
up to `maxsize` results based on a Most Recently USED (MRU)
algorithm.
	"""

	def decorating_function(f):

		cache = LRUCache(maxsize=maxsize, typed=typed)

		@wraps(f)
		def new_f(*args, **kwargs):
			key = _make_key(args, kwargs)
			if key not in cache:
				return f(*args, **kwargs)
			else:
				return cache[key]

		new_f.cache_clear = cache.clear
		new_f.cache_info = cache.info
		new_f.cache_replace = cache.update

		return new_f

	return decorating_function